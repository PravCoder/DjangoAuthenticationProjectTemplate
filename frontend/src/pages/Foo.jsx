import React, { useState, useEffect } from "react";
import api from "../api"; // Ensure this is the correct path to your api module
import { useNavigate } from "react-router-dom";
import FooForm from "../components/FooForm";


function Foo() {
    const [fooList, setFooList] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        getFoos();
    }, []); // Add dependency array to ensure this runs only once

    const getFoos = () => {
        api.get("/api/get-foo/")
            .then(res => {
                console.log(res);
                setFooList(res.data.foo_list); // Assuming res.data contains the list of foos
            })
            .catch(err => {
                console.error(err);
            });
    };

    return (
        <div>
            <p>All foos..</p>
            {fooList.length > 0 ? (
                fooList.map((foo, index) => (
                    <div key={index}>{foo}</div> // Adjust this based on the actual structure of your foo data
                ))
            ) : (
                <p>No foos found</p>
            )}

            <FooForm />
        </div>
    );
}

export default Foo;
