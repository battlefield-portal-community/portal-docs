# Portal Docs
<p align="center">
    <a href="https://github.com/battlefield-portal-community/portal-docs/actions/workflows/gen-docs.yml">  
    <img src="https://img.shields.io/github/actions/workflow/status/battlefield-portal-community/portal-docs/gen-docs.yml?branch=main&labelColor=011C26&label=Generate%20Docs%20Json&style=for-the-badge&color=26FFDF" alt="Generate Docs Json">
    </a>  
    <a href="https://github.com/battlefield-portal-community/portal-docs/actions/workflows/gh-pages.yaml">
    <img src="https://img.shields.io/github/actions/workflow/status/battlefield-portal-community/portal-docs/gh-pages.yaml?labelColor=011C26&label=Build%20GH-pages&style=for-the-badge&color=26FFDF" alt="Build GH pages">
    </a>
    <a href="https://github.com/battlefield-portal-community/portal-docs/actions/workflows/pages/pages-build-deployment">
    <img src="https://img.shields.io/github/deployments/battlefield-portal-community/portal-docs/github-pages?label=GH-pages%20deploy&style=for-the-badge&color=26FFDF&labelColor=011C26" alt="Deploy GH pages">  
    </a>        
</p> 

<p align="center"><img src="https://user-images.githubusercontent.com/22869882/172840336-7b48b7ca-63b4-4ca4-a054-3384547115da.png"> </p>


### Automated docs generation for [portal-helper](https://github.com/battlefield-portal-community/portal_helper) bot, 
### Uses github actions to compile the docs provided by https://portal.battlefield.com
#### Docs are saved in [docs](docs/) 
### Each doc follows the this class
```python
class CleanDoc(TypedDict):
    block_id: str
    block: str
    summary: str
    inputs: Optional[list]
    output: Optional[list]
```
