import React from 'react'
import styled from "styled-components"
import { Link } from 'react-router-dom'
import { SidebarData } from './SidebarData';
import SubMenu from './SubMenu';
import Img from '../../PIc/home.png';

const Sidebarnav = styled.nav`
  // height: 100vh;
  width:  250px;
  background-Color: #4f34eb;
`;

const Sidebarwrapp = styled.nav`
  background-Color: #4f34eb;
  color:  #fcba44;
  height: 100vh;
  width: 250px;
`;

const Navwrap = styled.nav`
justify-content: space-between;
padding-top:20px;
align-items: center;
display: flex;
background-Color: #4f34eb;
padding-left 3rem;
`

const Sidebar = () => {
  return (
    <>
    <div style={{width:"250px"}}>
      {/* <Navwrap>
      <img alt='' src={Img}/>
      </Navwrap> */}
        <Sidebarnav>
          <Sidebarwrapp>
            <Navwrap>
          <img alt='' src={Img}/>
          </Navwrap>
            {SidebarData.map((item, index) =>{
              return <SubMenu item={item} key={index} />;
            } )}
            
          </Sidebarwrapp>
        </Sidebarnav>
    </div>
    </>
  )
};
export default Sidebar;
