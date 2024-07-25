import React, { useState, useEffect } from 'react';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';
import review_icon from "../assets/reviewicon.png";

const Dealers = () => {
  const [dealersList, setDealersList] = useState([]);
  const [states, setStates] = useState([]);
  const [originalDealers, setOriginalDealers] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  const dealer_url = "/djangoapp/get_dealers";
  let dealer_url_by_state = "/djangoapp/get_dealers/";

  const filterDealers = async (state) => {
    dealer_url_by_state = dealer_url_by_state + state;
    const res = await fetch(dealer_url_by_state, {
      method: "GET"
    });
    const retobj = await res.json();
    if (retobj.status === 200) {
      let state_dealers = Array.from(retobj.dealers);
      setDealersList(state_dealers);
    }
  };

  const get_dealers = async () => {
    const res = await fetch(dealer_url, {
      method: "GET"
    });
    const retobj = await res.json();
    if (retobj.status === 200) {
      let all_dealers = Array.from(retobj.dealers);
      let states = [];
      all_dealers.forEach((dealer) => {
        states.push(dealer.state);
      });

      setStates(Array.from(new Set(states)));
      setDealersList(all_dealers);
      setOriginalDealers(all_dealers);
    }
  };

  useEffect(() => {
    get_dealers();
  }, []);

  const handleInputChange = (event) => {
    const query = event.target.value;
    setSearchQuery(query);
    const filtered = originalDealers.filter(dealer =>
      dealer.state.toLowerCase().includes(query.toLowerCase())
    );
    setDealersList(filtered);
  };

  const handleLostFocus = () => {
    if (!searchQuery) {
      setDealersList(originalDealers);
    }
  };

  let isLoggedIn = sessionStorage.getItem("username") != null ? true : false;

  return (
    <div>
      <Header />

      <table className='table'>
        <thead>
          <tr>
            <th>ID</th>
            <th>Dealer Name</th>
            <th>City</th>
            <th>Address</th>
            <th>Zip</th>
            <th>
              <input
                type="text"
                placeholder="Search states..."
                onChange={handleInputChange}
                onBlur={handleLostFocus}
                value={searchQuery}
              />
            </th>
            {isLoggedIn ? (
              <th>Review Dealer</th>
            ) : null}
          </tr>
        </thead>
        <tbody>
          {dealersList.map(dealer => (
            <tr key={dealer.id}>
              <td>{dealer.id}</td>
              <td><a href={'/dealer/' + dealer.id}>{dealer.full_name}</a></td>
              <td>{dealer.city}</td>
              <td>{dealer.address}</td>
              <td>{dealer.zip}</td>
              <td>{dealer.state}</td>
              {isLoggedIn ? (
                <td><a href={`/postreview/${dealer.id}`}><img src={review_icon} className="review_icon" alt="Post Review" /></a></td>
              ) : null}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dealers;
