# portal-docs
![image](https://user-images.githubusercontent.com/22869882/172840336-7b48b7ca-63b4-4ca4-a054-3384547115da.png)

### Automated docs generation for [portal-helper](https://github.com/battlefield-portal-community/portal_helper) bot, 
### Uses github actions to compile the docs provided by https://portal.battlefield.com
#### Docs are saved in [docs](docs/) 
### Each doc follows the this class
```python
class CleanDoc(TypedDict):
    block: str
    summary: str
    inputs: Optional[list]
    output: Optional[list]
```
