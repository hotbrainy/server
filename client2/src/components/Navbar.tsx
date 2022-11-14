import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShop, faUsers } from '@fortawesome/free-solid-svg-icons';
import { faList } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import '../scss/Navbar.scss';

const Navbar = () => {
    return (
        <div className="navbar">

            {/* Brand */}
            <div className="brand">
                <div className="icon">
                    <FontAwesomeIcon icon={faShop} />
                </div>

                <div className="name">
                    test
                </div>
            </div>

            {/* Links */}
            <div className="links">
                <Link to='#'>Data Analytics</Link>

                <Link to='#'> 
                    <FontAwesomeIcon icon={faUsers} />
                    Employees
                </Link>

                <Link to='#'>
                    <FontAwesomeIcon icon={faList} />
                    Projects
                </Link>

                <Link to='#'>Procurement</Link>

                <Link to='#'>Finance</Link>

                <Link to='#'>Competition Analysis</Link>
            </div>
        </div>
    )
}

export default Navbar;