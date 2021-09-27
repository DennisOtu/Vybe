import React, { Component } from "react";
import JoinRoomPage from "./joinRoomPage";
import CreateRoomPage from "./createRoomPage";
import Room from "./roomPage"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path ="/" component={CreateRoomPage} />
          <Route exact path ="/create" component={CreateRoomPage} />
          <Route path="/join" component={JoinRoomPage} />
          <Route path="/room/:roomCode" component={Room} />
        </Switch>
      </Router>
    );
  }
}
