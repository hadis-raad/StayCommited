import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Habits.css';

const Habits = () => {
  const [habits, setHabits] = useState([]);
  const [name, setName] = useState('');
  const [frequency, setFrequency] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchHabits();
  }, []);

  const fetchHabits = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/habits/');
      setHabits(response.data);
    } catch (error) {
      console.error('There was an error fetching the habits!', error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/habits/', {
        name,
        frequency,
        user_id: 1,  // Assuming you have a user with ID 1
        goal_id: 1   // Assuming you have a goal with ID 1
      });
      setMessage('Habit created successfully!');
      setName('');
      setFrequency('');
      fetchHabits();
    } catch (error) {
      setMessage('Error creating habit. Please try again.');
      console.error('There was an error creating the habit!', error);
    }
  };

  return (
    <div>
      <h1>Habits</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Frequency:</label>
          <input
            type="text"
            value={frequency}
            onChange={(e) => setFrequency(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create Habit</button>
      </form>
      {message && <p>{message}</p>}
      <h2>Habits List</h2>
      <ul>
        {habits.map(habit => (
          <li key={habit.habit_id}>
            {habit.name} - {habit.frequency}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Habits;
