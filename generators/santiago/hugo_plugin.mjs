
// @ts-check
/**
 * @param {import('typedoc-plugin-markdown').MarkdownApplication} app
 */
function emitHugoIndexInfo(app) {
    const INFO = `---
draft: false
geekdocCollapseSection: true
type: typedoc_gen
---
`
return INFO
}



// @ts-check
/**
 * @param {import('typedoc-plugin-markdown').MarkdownApplication} app
 */
function emitHugoInfo(app) {
    const INFO = `---
draft: false
type: typedoc_gen
---
`
return INFO
}

// @ts-check
/**
 * @param {import('typedoc-plugin-markdown').MarkdownApplication} app
 */
export function load(app) {
  app.renderer.markdownHooks.on(
    'index.page.begin', () => emitHugoIndexInfo(app)
  );
  app.renderer.markdownHooks.on(
    'page.begin', () => emitHugoInfo(app)
  );
}