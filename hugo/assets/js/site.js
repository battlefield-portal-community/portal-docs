/* The documentation's small amount of behavior: the menu drawer on narrow
   screens, the search dialog, the buttons on code blocks, and which heading
   the table of contents marks as current. */

(() => {
  "use strict";

  /* ------------------------------------------------------------ drawer */

  const drawer = document.querySelector("[data-drawer]");
  const menuButton = document.querySelector("[data-drawer-open]");
  const scrim = document.querySelector("[data-scrim]");

  const setDrawer = (open) => {
    if (!drawer) return;
    document.documentElement.classList.toggle("drawer-open", open);
    if (menuButton) menuButton.setAttribute("aria-expanded", String(open));
  };

  if (menuButton) {
    menuButton.addEventListener("click", () => {
      setDrawer(!document.documentElement.classList.contains("drawer-open"));
    });
  }
  if (scrim) scrim.addEventListener("click", () => setDrawer(false));
  drawer?.addEventListener("click", (event) => {
    if (event.target.closest("a")) setDrawer(false);
  });
  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setDrawer(false);
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) setDrawer(false);
  });

  /* ------------------------------------------------------------ search */

  const dialog = document.querySelector("[data-search]");
  const input = dialog?.querySelector("[data-search-input]");
  const list = dialog?.querySelector("[data-search-results]");
  const openers = document.querySelectorAll("[data-search-open]");

  let index = null;
  let indexPromise = null;
  let results = [];
  let selected = -1;

  const loadIndex = () => {
    if (indexPromise) return indexPromise;
    const url = dialog?.dataset.search;
    indexPromise = fetch(url, { credentials: "same-origin" })
      .then((response) => (response.ok ? response.json() : []))
      .then((data) => {
        index = Array.isArray(data) ? data : [];
        return index;
      })
      .catch(() => {
        index = [];
        return index;
      });
    return indexPromise;
  };

  const escapeHtml = (text) =>
    text.replace(
      /[&<>"']/g,
      (character) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[character],
    );

  const terms = (query) =>
    query
      .toLowerCase()
      .split(/[^\p{L}\p{N}_]+/u)
      .filter((term) => term.length > 0);

  const countOf = (haystack, needle) => {
    let count = 0;
    let at = haystack.indexOf(needle);
    while (at !== -1 && count < 12) {
      count += 1;
      at = haystack.indexOf(needle, at + needle.length);
    }
    return count;
  };

  // Where the first term appears in the page's text, and a little around it.
  const excerpt = (entry, words) => {
    const text = entry.c || "";
    const lower = text.toLowerCase();
    let at = -1;
    for (const word of words) {
      const found = lower.indexOf(word);
      if (found !== -1 && (at === -1 || found < at)) at = found;
    }
    if (at === -1) return text.slice(0, 150);
    const from = Math.max(0, at - 45);
    return `${from > 0 ? "…" : ""}${text.slice(from, from + 170).trim()}`;
  };

  const highlight = (text, words) => {
    if (!words.length) return escapeHtml(text);
    const pattern = words
      .filter((word) => word.length > 1)
      .map((word) => word.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
      .join("|");
    if (!pattern) return escapeHtml(text);
    const split = new RegExp(`(${pattern})`, "gi");
    return text
      .split(split)
      .map((part, position) =>
        position % 2 === 1
          ? `<mark>${escapeHtml(part)}</mark>`
          : escapeHtml(part),
      )
      .join("");
  };

  const search = (query) => {
    const words = terms(query);
    if (!index || !words.length) return [];
    const found = [];
    for (const entry of index) {
      const title = (entry.t || "").toLowerCase();
      const section = (entry.s || "").toLowerCase();
      const text = (entry.c || "").toLowerCase();
      let score = 0;
      for (const word of words) {
        if (title.startsWith(word)) score += 60;
        else if (title.includes(` ${word}`)) score += 40;
        else if (title.includes(word)) score += 22;
        if (section.includes(word)) score += 8;
        const inText = countOf(text, word);
        if (inText) score += Math.min(inText, 8) * 2 + 4;
      }
      if (score > 0) {
        // Pages that match every word come before pages that match some.
        const matched = words.filter(
          (word) =>
            title.includes(word) || section.includes(word) || text.includes(word),
        ).length;
        if (matched === words.length) score += 40;
        found.push({ entry, score });
      }
    }
    found.sort((a, b) => b.score - a.score);
    return found.slice(0, 20).map((item) => item.entry);
  };

  const closeSearch = () => {
    if (dialog?.open) dialog.close();
  };

  const openSearch = () => {
    if (!dialog) return;
    setDrawer(false);
    if (!dialog.open) dialog.showModal();
    loadIndex();
    input?.focus();
    input?.select();
  };

  const render = (query) => {
    if (!list) return;
    results = search(query);
    selected = results.length ? 0 : -1;
    if (!query.trim()) {
      list.innerHTML = "";
      return;
    }
    if (!results.length) {
      list.innerHTML = `<li class="search__empty">${
        index ? "Nothing found." : "Loading the index…"
      }</li>`;
      return;
    }
    const words = terms(query);
    list.innerHTML = results
      .map(
        (entry, position) => `
        <li>
          <a class="search__result" href="${escapeHtml(entry.u)}" data-result
             aria-selected="${position === 0}">
            <span class="search__result-title">
              ${highlight(entry.t || entry.u, words)}
              ${entry.s ? `<span>${escapeHtml(entry.s)}</span>` : ""}
            </span>
            <span class="search__result-text">${highlight(
              excerpt(entry, words),
              words,
            )}</span>
          </a>
        </li>`,
      )
      .join("");
  };

  const move = (step) => {
    const links = list?.querySelectorAll("[data-result]");
    if (!links?.length) return;
    selected = (selected + step + links.length) % links.length;
    links.forEach((link, position) =>
      link.setAttribute("aria-selected", String(position === selected)),
    );
    links[selected].scrollIntoView({ block: "nearest" });
  };

  for (const opener of openers) {
    opener.addEventListener("click", (event) => {
      event.preventDefault();
      openSearch();
    });
  }

  if (dialog && input) {
    let timer;
    input.addEventListener("input", () => {
      clearTimeout(timer);
      timer = setTimeout(() => render(input.value), 90);
    });
    input.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        // One Escape, whatever is in the field: the dialog closes and the
        // input is emptied with it.
        event.preventDefault();
        closeSearch();
        return;
      }
      if (event.key === "ArrowDown") {
        event.preventDefault();
        move(1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        move(-1);
      } else if (event.key === "Enter") {
        const link = list?.querySelector('[aria-selected="true"]');
        if (link) {
          event.preventDefault();
          window.location.href = link.getAttribute("href");
        }
      }
    });
    dialog.addEventListener("close", () => {
      if (input) input.value = "";
      if (list) list.innerHTML = "";
      results = [];
      selected = -1;
    });
    dialog.addEventListener("click", (event) => {
      // A click on the backdrop, outside the panel's own box.
      if (event.target === dialog) closeSearch();
    });
    loadIndex();
  }

  window.addEventListener("keydown", (event) => {
    const typing =
      event.target instanceof HTMLElement &&
      (event.target.isContentEditable ||
        ["INPUT", "TEXTAREA", "SELECT"].includes(event.target.tagName));
    if (typing) return;
    if (event.key === "/" || (event.key.toLowerCase() === "k" && event.metaKey)) {
      event.preventDefault();
      openSearch();
    }
  });

  /* --------------------------------------------------------- code blocks */

  const label = (code) =>
    (code.dataset.lang || code.className || "").replace(/^language-/, "").trim();

  for (const block of document.querySelectorAll(".highlight")) {
    const code = block.querySelector("code");
    if (!code) continue;
    const tools = document.createElement("div");
    tools.className = "code-tools";
    const language = label(code);
    if (language) {
      const lang = document.createElement("span");
      lang.className = "code-lang";
      lang.textContent = language;
      tools.append(lang);
    }
    const button = document.createElement("button");
    button.type = "button";
    button.className = "code-copy";
    button.textContent = "Copy";
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(code.innerText);
        button.textContent = "Copied";
        button.dataset.copied = "true";
        setTimeout(() => {
          button.textContent = "Copy";
          button.dataset.copied = "false";
        }, 1600);
      } catch {
        button.textContent = "Press ⌘C";
      }
    });
    tools.append(button);
    block.append(tools);
  }

  /* ----------------------------------------------------------------- toc */

  const toc = document.querySelector("[data-toc]");
  if (toc && "IntersectionObserver" in window) {
    const links = new Map();
    for (const link of toc.querySelectorAll('a[href^="#"]')) {
      const id = decodeURIComponent(link.getAttribute("href").slice(1));
      if (id) links.set(id, link);
    }
    const headings = [...links.keys()]
      .map((id) => document.getElementById(id))
      .filter(Boolean);
    if (headings.length) {
      const visible = new Set();
      const observer = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting) visible.add(entry.target.id);
            else visible.delete(entry.target.id);
          }
          const current =
            headings.find((heading) => visible.has(heading.id)) || null;
          for (const [id, link] of links) {
            link.classList.toggle("is-active", current?.id === id);
          }
        },
        { rootMargin: "-72px 0px -70% 0px" },
      );
      for (const heading of headings) observer.observe(heading);
    }
  }

  /* Keep the current page visible in the sidebar when the page opens. A page
     inside the block catalog is centred by the catalog itself, further down. */
  const active = document.querySelector(".sidenav [aria-current='page']");
  if (active && !active.closest("[data-sidenav-scroll]")) {
    const sidebar = active.closest(".sidebar");
    if (sidebar) {
      const offset =
        active.getBoundingClientRect().top - sidebar.getBoundingClientRect().top;
      if (offset > sidebar.clientHeight - 80 || offset < 0) {
        sidebar.scrollTop += offset - sidebar.clientHeight / 3;
      }
    }
  }

  /* ------------------------------------------------------ block catalog */

  /* The block reference is 271 names in a fixed box. Put the block you are
     reading in the middle of that box, and let the filter cut the list down
     to the handful you are actually looking for. */
  for (const field of document.querySelectorAll("[data-sidenav-filter]")) {
    const catalog = field.closest(".sidenav__catalog");
    const scroller = catalog?.querySelector("[data-sidenav-scroll]");
    const empty = catalog?.querySelector("[data-sidenav-empty]");
    const list = scroller?.querySelector("ul");
    if (!scroller || !list) continue;

    const centre = () => {
      const current = scroller.querySelector("[aria-current='page']");
      if (!current || !scroller.clientHeight) return;

      /* First bring the whole block into view in whatever contains it — the
         section's own header, the filter and the window — aligning its top
         with the container's top so no row is cut in half. */
      const outer = scroller.closest(".sidebar, .sidebar-drawer");
      const block = scroller.closest("details") || scroller;
      if (outer) {
        const delta =
          block.getBoundingClientRect().top - outer.getBoundingClientRect().top;
        if (
          block.offsetHeight <= outer.clientHeight &&
          (delta < 0 || block.offsetHeight > outer.clientHeight - delta)
        ) {
          outer.scrollTop = Math.max(0, outer.scrollTop + delta);
        }
      }

      /* Measured, not offsetTop: the scroller is not the offset parent, so
         offsetTop would be an absolute page coordinate. */
      const offset =
        current.getBoundingClientRect().top -
        scroller.getBoundingClientRect().top +
        scroller.scrollTop;
      scroller.scrollTop =
        offset - scroller.clientHeight / 2 + current.offsetHeight / 2;
    };

    centre();
    /* Fonts land after first paint and change every row's height, so the
       centring that matters is the one measured once they are in. */
    window.addEventListener("load", centre);

    const rows = [...list.children];
    field.addEventListener("input", () => {
      const needle = field.value.trim().toLowerCase();
      let shown = 0;
      for (const row of rows) {
        const hit = !needle || row.textContent.toLowerCase().includes(needle);
        row.hidden = !hit;
        if (hit) shown += 1;
      }
      if (empty) empty.hidden = shown > 0;
      if (needle) scroller.scrollTop = 0;
    });

    /* A filter that survives a reload is a filter nobody remembers setting. */
    field.value = "";
  }
})();
