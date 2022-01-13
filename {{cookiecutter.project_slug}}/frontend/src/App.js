import './App.css'
{% if cookiecutter.use_users_example == 'y' %}
import { useState, useEffect } from 'react'

const App = () => {
	const [items, setItems] = useState([])

	useEffect(() => {
		const fetchUsers = () => {
			fetch('http://localhost:8000/api/users/', {mode: 'cors'})
				.then(results => results.json())
				.then(data => {
					setItems(data)
				}
			)
		}
	
		fetchUsers()

	}, [])

	return (
		<div className='App'>
			{items.map((item) => (
				<User item={item} key={item.id}/>	
			))}
		</div>
	)
}

const User = ({item}) => {
	return (
		<div className={'user'}>
			<h2 className={item.is_staff ? 'staff' : null} title={item.date_joined}>
				{item.username}
			</h2>
			<h3>{item.email}</h3>
		</div>
	)
}
{% else %}
const App = () => {
  return (
    <div className='App'>
      <h1>Hello!</h1>
    </div>
  )
}
{% endif %}

export default App
