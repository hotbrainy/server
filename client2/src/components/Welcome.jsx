import '../scss/Welcome.scss';

const Welcome = () => {

    return (
        <div className="App">
        <header className="App-header">
          <div className="row">
            <div className="col-sm-6">
              <h1>Home</h1>
              <p className="lead">Start</p>
              <h3>
                <a href="/home"><button className="btn btn-primary btn-lg">Get home</button></a>
                <a href="#"><button className="btn btn-outline-warning btn-lg">About company</button></a>
              </h3>
              <h3>
                <a href="#"><button className="btn btn-primary btn-lg">Blog website</button></a>
                <a href="@"><button className="btn btn-outline-warning btn-lg">Sign Up</button></a>
              </h3>
            </div>
            <div className="col-sm-6 hidden-sm hidden-xs">
              <img className="rounded img-fluid" src="https://images.unsplash.com/photo-1584714268709-c3dd9c92b378?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=927&q=80" alt="Front Photo of Musical Band" />
            </div>
          </div>
        </header>
    </div>
    )

}

export default Welcome;