import React, { useState, useEffect } from "react";

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetching data from the FastAPI backend
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch("http://localhost:8000/items");
        if (!response.ok) {
          throw new Error("Failed to fetch items");
        }
        const data = await response.json();
        setItems(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;
