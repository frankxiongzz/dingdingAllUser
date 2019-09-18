# dingdingAllUser
钉钉只有遍历部门、子部门、部门下所有员工的信息的api，没有遍历所有员工的API，所以写了个递归来获取公司所有员工
```
from dingtalk import SecretClient
 
def get_all_user_by_departments(client, all_departments):
 
    if all_departments is None:
        return
    else:
        for department in all_departments:
            # 打印该部门的成员
            userList = client.user.simple_list(department_id = department['id'])
            for user in userList['userlist']:
                print(user)
 
            # 递归下去
            all_child_departments = client.department.list(department['id'])
            get_all_user_by_departments(client, all_child_departments)
 
if __name__ == '__main__':
 
    CORP_ID = "xxx"
    APPKEY = "xxx"
    SECRET = "xxx"
    AGENT_ID = "xxx"
    client = SecretClient(APPKEY, SECRET)
 
    all_departments = client.department.list()
    get_all_user_by_departments(client, all_departments)
```
