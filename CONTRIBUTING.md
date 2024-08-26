First off, thanks for taking the time to contribute! 🎉🎉

This file contains a few guidelines on how to contribute to the community made portal docs hosted at [docs.bfportal.gg](https://docs.bfportal.gg)

These are not rules but just some suggestion, so feel free to propose any change in the project

{{< toc >}}

## Architecture of the docs

The project is split into two parts:

- The docs themselves, written in markdown and located in the `docs` folder
- The website, built with [Geekdocs](https://geekdocs.de/) and located in the `hugo` folder

---

The **docs** are also split into two parts:

- The docs that are hand-written and located in the **`docs`** folder
- The docs that are generated using the **`portal_blocks_documentation`** module.

  - The process to generate new docs for portal blocks is pretty much automated

  - The official documentation for each block is retrieved and saved to the **`docs/portal_blocks/<block_name>/docs/official.md`** folder

    - Any changes to this file **will be overwritten** when the docs are regenerated

  - The **`docs/portal_blocks/<block_name>/docs/extra.md`** file is where you can add extra information about the block
    - This file will **not be overwritten** when the docs are regenerated

## Contributing to the docs

### Local environment setup

- Setup `hugo` on your machine, you can follow the [official guide](https://gohugo.io/installation/)
- Clone this repository (requires [git](https://git-scm.com/))
  
  ```shell
  git clone https://github.com/battlefield-portal-community/portal-docs
  ```

- Change directory to the root directory of the cloned repository and run
  
  ```shell
   hugo server -D
  ```

### Contribute to hand written docs

- If You want to add a new tutorial/guide run,

```shell
hugo new content [guide|tutorial]/<name_of_tutorial_or_guide>
```

- then you should be able to find the file in **`docs/[guides|tutorials]/<name_of_tutorial_or_guide>/_index.md`**

### Contribute to Portal Blocks Documentation

- If you wish to add extra information to the portal blocks documentation
- In **`docs/portal_blocks/`** Find the block which you want to add information to.
- In that folder You will see two things.
  - `index.md` which is the root of the block documentation
  - A folder called `docs` which contains the documentation for the block
    - In the `docs` folder find/create a file called `extra.md` and add the extra information there.
    - All the new information will be added to the bottom of the block documentation page.
- The code which generates the block documentation structure can be found at `/generators`

## TODOs (PRs welcome :D )

- [x] Add a section on how to contribute to the docs
- [ ] Add a section on how to contribute to the website
- [ ] Add a section on how to contribute to the `portal_blocks_documentation` module
