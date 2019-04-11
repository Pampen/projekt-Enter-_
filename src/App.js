import React, { Component } from 'react';
import './styles/style.css';
import sendMessage from './utilities/connect.js'
import ButtonContainer from './components/button-container'
import GameScreen from './components/game-screen'
import Terminal from './components/terminal'
import Modal from './components/Modal'
import apple from './assets/apple.jpg'

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      title: "Beach",
      description: "The door closes behind you, leaving you alone in the darkness. Suddenly, everything lights up and you find yourself on the beach. There's a Lighthouse right infront of you up the hill(NORTH), a shipwreck by the coast(EAST) and what looks to be a shed to your left(WEST) by the seaside. Which way do you decide to go?",
      chatboxText: [],
      inventory: {
        firstObject: false,
        secondObject: false
      },
      level: 'BEACH'
    }
    this.updateState=this.updateState.bind(this)
  }

  updateState(inputElementValue) {
    sendMessage(inputElementValue, this.state).then(response => {
      const newTitle = response.pageChanges.levelTitle || null
      const newDescription = response.pageChanges.levelDescription || null
      const newChatboxText = response.pageChanges.levelChatboxText || null
      const newGameState = {}
      newGameState.inventory = response.state.inventory
      newGameState.level = response.state.level
      if (newTitle) {
        newGameState.title = newTitle;
      };
      if (newDescription) {
        newGameState.description = newDescription;
      };
      if (newChatboxText) {
        const currentChatboxText = this.state.chatboxText;
        currentChatboxText.push(newChatboxText);
        newGameState.chatboxText = currentChatboxText;
      }
      this.setState(newGameState);
      console.log(this.state);
    })
};

showMapModal = () => {
    this.setState({
      ...this.state,
      show: !this.state.show
    });
}

  render() {
    return (
      <main id="wrapper">
        <div className="container">
          <ButtonContainer handleMapClick={this.showMapModal}/>
          <div className="game-container">
            <GameScreen
              title={this.state.title}
              description={this.state.description}
              chatboxText={this.state.chatboxText}
            />
            <Terminal
            updateState={this.updateState}
            />
            <Modal 
              onClose={this.showMapModal}
              show={this.state.show}>
                <img src={apple} alt="An apple"/>
            </Modal>
        </div> 
      </div>
    </main>
    );
  }
}

export default App;