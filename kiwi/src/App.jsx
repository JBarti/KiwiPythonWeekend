import React, { Component } from 'react';
import './App.css';
import axios from 'axios'

class App extends Component {
  state = { departure: 'Something', arival: 'Something', price: '0', data: [] }

  handleChange = (ev) => {
    this.setState({ [ev.target.name]: ev.target.value })
  }

  submit = () => {
    axios.get('http://127.0.0.1:5000/search', {
      params:
      {
        source: this.state.departure,
        destination: this.state.arival,
        price: this.state.price
      }
    }).then(data => {
      console.log(data)
      this.setState({ data: data.data })
    })
  }

  render() {
    return (<div className='app'>
      <input onChange={this.handleChange} name='departure' value={this.state['departure']} placeholder='departure' />
      <br />
      <input onChange={this.handleChange} name='arival' value={this.state['arival']} placeholder='arival' />
      <br />
      <input onChange={this.handleChange} name='price' value={this.state['price']} type='number' />
      <br />
      <button onClick={this.submit}>SUBMIT</button>
      <table>
        <tr>
          <th>arival</th>
          <th>departure</th>
          <th>price</th>
          <th>carrier</th>
          <th>traveling_time</th>
        </tr>
        {this.state.data.map(data => {
          return <tr>
            <th>{data.arival}</th>
            <th>{data.departure}</th>
            <th>{data.price}</th>
            <th>{data.carrier}</th>
            <th>{data.traveling_time}</th>
          </tr>
        })}
      </table>

    </div>)
  }
}

export default App;