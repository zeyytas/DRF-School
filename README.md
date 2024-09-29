
<h1>Introduction</h1> 

DRF-school provides couple of filtering, grouping and sorting actions on Exam database.

## Installation

First, start by cloning the repository:

```
git clone https://github.com/zeyytas/DRF-school.git
```

Recommended to use `virtualenv` for development:

- Start by installing `virtualenv` if you don't have it
```
pip install virtualenv
```

- Create a virtual environment
```
virtualenv env
```

- Enable the virtual environment
```
source env/bin/activate
```

- Install the python dependencies on the virtual environment
```
pip install -r requirements.txt
```

## Action
<small>
   
GET         /api/v1/exam? </small>

## Attributes

<small>
   
   - date_from and date_to

   ```e.g.   ?date_from=2017-05-17&date_to=2017-05-19```
   
   - name

   ```e.g.   ?name=mathematics,art```


   - student_name

   ```e.g.   ?student_name=Lisa-Simpson,Bart-Simpson```
   
   
   - teacher_name

   ```e.g.   ?teacher_name=Anna-Smith```
   
   - score_from and score_to

   ```e.g.   ?score_from=45&score_to=48```

   - sort_by </br>
   The default ordering is ascending. If you want to change the sort order to descending, append :desc to the field.

   ```e.g. ?sort_by=score:desc```

   - show </br>
   This attribute provides the field you want to be shown as a result
   
   ```e.g  ?show=teacher_name```
   
   - group_by </br>
   This attribute provides broken down attribute with which field
   
   ```e.g  ?group_by=student_name,date```
   
   - grade </br>
   This attribute should be used with group_by
   ```
     0< grade <20 F 
     20<= grade <50 E 
     50<= grade <70 D 
     70<= grade <80 C 
     80<= grade <90 B
     90<= grade <=100 A
   ```
   
   ```e.g.   ?show=grade&group_by=student_name,course_name``` </br>
   ```e.g.   ?show=grade&student_name=Lisa-Simpson,Bart-Simpson&group_by=student_name,course_name```
</small>
