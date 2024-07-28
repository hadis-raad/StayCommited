import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Goals.css';

const Goals = () => {
  const [goals, setGoals] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [status, setStatus] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchGoals();
  }, []);

  const fetchGoals = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/goals/');
      setGoals(response.data);
    } catch (error) {
      console.error('There was an error fetching the goals!', error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/goals/', {
        title,
        description,
        start_date: startDate,
        end_date: endDate,
        status,
        user_id: 1  // Assuming you have a user with ID 1
      });
      setMessage('Goal created successfully!');
      setTitle('');
      setDescription('');
      setStartDate('');
      setEndDate('');
      setStatus('');
      fetchGoals();
    } catch (error) {
      setMessage('Error creating goal. Please try again.');
      console.error('There was an error creating the goal!', error);
    }
  };

  return (
    <div>
      <h1>Goals</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Start Date:</label>
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            required
          />
        </div>
        <div>
          <label>End Date:</label>
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Status:</label>
          <input
            type="text"
            value={status}
            onChange={(e) => setStatus(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create Goal</button>
      </form>
      {message && <p>{message}</p>}
      <h2>Goals List</h2>
      <ul>
        {goals.map(goal => (
          <li key={goal.goal_id}>
            {goal.title} - {goal.description} - {goal.start_date} - {goal.end_date} - {goal.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Goals;
