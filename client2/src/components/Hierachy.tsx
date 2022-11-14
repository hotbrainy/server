import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faUserCircle, faUser } from "@fortawesome/free-regular-svg-icons";
import { faShop, faAdd, faMinus, faArrowRight } from "@fortawesome/free-solid-svg-icons"
import  '../scss/Hierachy.scss';
import Navbar from "./Navbar";
import SampleMember from "./SampleMember";
import { useEffect, useState } from "react";
import axios from "axios";

interface IAll {
    users: IProps[]
}

interface IProps {
    first_name? : string,
    email? : string,
    role? : string
}



interface IState{
    ok: boolean;
    result: IAll
}

const Hierachy = () => {
    const [users, setUsers] = useState<IState>()

    useEffect(()=>{
      axios.get('/api/users').then(response => {
        console.log("SUCCESS", response.data)
        setUsers(response.data)
      }).catch(error => {
        console.log(error)
      })
  
    }, [])

    
    return (
        <>
            <Navbar />
            <div className="hierachy">

                <div className="title">Hierarchy</div>
                <div className="main">

                    {/* Branches */}
                    <div className="section branches">
                        <div className="branch">
                            <div className="icon">
                                <FontAwesomeIcon icon={faShop} />
                            </div>
                            
                            <div className="info">
                                <div>test</div>
                                <div>Lorem, ipsum.</div>
                            </div>
                        </div>
                    </div>

                    {/* Members */}
                    <div className="section members">

                        {/* Lead (black bg) */}
                        <div className="lead">
                            <div className="icons">
                                <div className="profile">
                                    <FontAwesomeIcon icon={faUser} />
                                </div>
                                <div className="ctrls">
                                    <FontAwesomeIcon icon={faMinus} id="remove" />
                                    <FontAwesomeIcon icon={faAdd} id="add" />
                                </div>
                            </div>

                            <div className="info">
                                <div>qwert@2</div>
                                <div>Lorem ipsum.</div>
                            </div>
                        </div>


                        {/* Other cards */}
                        <div className="staff">
                            {
                                 users?.result.users.map( user => {
                                    return (
                                        <SampleMember first_name={user.first_name} email={user.email} role={user.role}/>
                                    )
                                })
                            }
                            {/* <SampleMember first_name={getMessage.ok}/> */}
                        </div>
                    </div>

                    <div className="section blank"></div>

                </div>

            </div>
        </>
    )
};

export default Hierachy;