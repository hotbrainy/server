import { faUserCircle } from "@fortawesome/free-regular-svg-icons";
import { faArrowRight, faMinus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState }  from "react";

interface IProps {
    first_name? : string,
    email? : string,
    role? : string
}


let SampleMember:React.FC<IProps> = ({first_name, email, role}) => {


    return (
        <React.Fragment>
            <div className="member">
                <div className="icons">
                    <div className="profile">
                        <FontAwesomeIcon icon={faUserCircle} />
                    </div>
                    <div className="ctrls">
                        <FontAwesomeIcon icon={faMinus} id="remove" />
                        <FontAwesomeIcon icon={faArrowRight} id="forward" />
                    </div>
                </div>
                <div className="info">
                    <div>{first_name}</div>
                    <div>{email}</div>
                    <div>{role}</div>
                </div>
            </div>
        </React.Fragment>
    )
};



export default SampleMember;

