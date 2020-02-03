# API

Concept Guidance:
* [What is an API?](./https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API?](./https://www.sitepoint.com/developers-rest-api/)
* [Microservices](./https://smartbear.com/solutions/microservices/)

### [0. Gather data from an API](./0-gather_data_from_an_API.py)
> Write a Python script that, using this [REST API](./https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress
> Reqs:
> * use urllib or requests module
> * must accept an integer as a parameter, which is the employee ID
> * must display on the standard output the employee TODO list progress
> Example:
> ``` sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
  Employee Ervin Howell is done with tasks(8/20):
       distinctio vitae autem nihil ut molestias quo
       voluptas quo tenetur perspiciatis explicabo natus
       aliquam aut quasi
       veritatis pariatur delectus
       nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
       repellendus veritatis molestias dicta incidunt
       excepturi deleniti adipisci voluptatem et neque optio illum ad
       totam atque quo nesciunt
  sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
  Employee Patricia Lebsack is done with tasks(6/20):
       odit optio omnis qui sunt
       doloremque aut dolores quidem fuga qui nulla
       sint amet quia totam corporis qui exercitationem commodi
       sequi dolorem sed
       eum ipsa maxime ut
       tempore molestias dolores rerum sequi voluptates ipsum consequatur```

### [1. Export to CSV](./1-export_to_CSV.py)
