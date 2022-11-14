import React, { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

const SideBarLink = styled(Link)`
    display: flex;
    color: #fafafc;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    list-style: none;
    height: 60px;
    text-decoration: none;
    font-size: 18px;
`;

const SidebarLable = styled.span`
    margin-left:12px;
`

const DropdownLink = styled(Link)`
    background-Color #acacbd; 
    height:60px;
    padding-left:3rem;
    display:flex;
    align-items:center;
    color: white;
    font-size:18px;
    text-decoration: none;
`

const SubMenu = ({item}) => {
    const [subnav, Setsubnav]  = useState(false)

    const Showsubnav = () => Setsubnav(!subnav)
    return(
        <>
        
        <SideBarLink to={item.path} onClick={item.subNav && Showsubnav}>
            <div>
                {item.icons}
                <SidebarLable>{item.title}</SidebarLable>
            </div>
            <div>
                {subnav && item.subNav
                ? item.iconOpen 
                : item.subNav  
                ? item.iconClosed 
                : null}
            </div>  
        
        </SideBarLink>

        {subnav && item.subNav.map((item, index) => {
            return (
                <DropdownLink to={item.path} key={index}>
                    {item.icons}
                <SidebarLable>{item.title}</SidebarLable>
                </DropdownLink>
            )
        })}

        </>
    );
};

export default SubMenu