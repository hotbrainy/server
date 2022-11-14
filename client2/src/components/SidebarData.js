import React from "react";
import * as FaIcons from "react-icons/fa"
import * as AiIcons from "react-icons/ai"
import * as GiIcons from "react-icons/gi"
import * as RiIcons from "react-icons/ri"
import * as BiIcons from "react-icons/bi"


export const SidebarData  = [
    {
        title: 'Overview',
        // path: '/overview',
        icons: <AiIcons.AiOutlineBarChart/>,
        iconOpen : <RiIcons.RiArrowUpFill/>,
        iconClosed: <RiIcons.RiArrowDownFill/>,


        subNav : [
            {
                title: 'Users',
                path: 'overview/users',
                icons: <BiIcons.BiAddToQueue/>
            },
            {
                title: 'Revenue',
                path: 'overview/revenue',
                icons: <BiIcons.BiAdjust/>
            },
        ]
    },


    {
        title: 'Products',
        path: '/products',
        icons: <AiIcons.AiFillAlert/>,
    },

    {
        title: 'Management',
        path: '/management',
        icons: <AiIcons.AiFillAlipaySquare/>,
    },

    {
        title: 'Support',
        path: '/support',
        icons: <BiIcons.BiAlarmAdd/>,
    },

    {
        title: 'Contact',
        path: '/contatc',
        icons: <FaIcons.FaAddressBook/>,
    },



    ]
