import React, {useState, useEffect} from 'react';
import TodoDataService from '../services/todos';
import { Link } from 'react-router-dom';

import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

import Alert from 'react-bootstrap/Alert';

import moment from 'moment';


// We import useState to create a todos state variable. We import useEffect (which we will describe later) and also
// import TodoDataService and Link.

const TodosList = props => {
  const [todos, setTodos] = useState([]);

  // useEffect to retrieveTodos
  // Next, we add the useEffect hook and the retrieveTodos as shown:
  useEffect(() => {
    retrieveTodos();
  }, [props.token]);

  const retrieveTodos = () => {
    TodoDataService.getAll(props.token)
      .then(response =>{
        setTodos(response.data);
      })
      .catch(e=>{
        console.log(e)
      });
  }

  return(
    <Container>
      {props.token==null || props.token===""?(
        <Alert variant='warnings'>
          You are not logged in. Please <Link to={"/login"}>login</Link> to see your todos.
        </Alert>
      ):(
        <div>
          {todos.map((todo)=>{

            return(
              <Card key={todo.id} className='mb-3'>
                <Card.Body>
                  <div>
                    <Card.Title>{todo.title}</Card.Title>
                    <Card.Text><b>Memo:</b>{todo.memo}</Card.Text>
                    <Card.Text>Date created:{moment(todo.created).format("Do MMMM YYYY")}</Card.Text>
                  </div>
                  <Link to={{
                    pathname:"/todos/"+todo.id,
                    state: {
                      currentTodo:todo
                    }
                  }}>
                    <Button variant='outline-info' className='me-2'>
                      Edit
                    </Button>
                  </Link>
                  <Button variant='outline-danger'>
                    Delete
                  </Button>
                </Card.Body>
              </Card>
            )
          })}
        </div>
      )
      }
    </Container>
  );
}

// TodosList is a functional component that receives and uses props. We use the
// todos state variables. Note that todos is default set to an empty array useState([])

export default TodosList;