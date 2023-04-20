import { Link } from 'react-router-dom'
import { FaSearch } from "react-icons/fa"
import { FaUserAlt } from "react-icons/fa";

function Nav() {
    const my_4a = {
        backgroundColor: "#3399ff",
        display: "flex",
        flexDirection: "row",
        fontFamily: "Geneva",
        fontWeight: "bold",
        alignItems: "center",
        //position: "fixed"
    };
    
    return (
        <nav >
            <div style={my_4a}>
              
                <Link to="/" >
                  <img src={`${process.env.PUBLIC_URL}/logo.jpg`} style={{width:160}}/> 
                </Link>

                <ul>
                    <Link style={{color: "#ffffff"}} to="/">
                        HOME
                    </Link>
                </ul>
                <ul>
                    <Link style={{color: "#ffffff"}} to="/inputsentence">
                        INPUT SENTENCE
                    </Link>
                </ul>
                <ul>
                    <Link style={{color: "#ffffff"}} to="/inputfile">
                        INPUT FILE
                    </Link>
                </ul>
             
                <ul style={{marginLeft: 700}}>
                    <button type="button" style={{backgroundColor: "#3399ff"}}><FaUserAlt size={28}/>Log In</button>
                </ul>
            </div>
        </nav>
    );
}

export default Nav;