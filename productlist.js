import React, { useState, useEffect } from 'react';
import api from '../api';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        api.get('/products').then(response => setProducts(response.data));
    }, []);

    return (
        <div>
            <h1>Products</h1>
            <div>
                {products.map(product => (
                    <div key={product.id}>
                        <img src={product.image_url} alt={product.title} width="100" />
                        <h2>{product.title}</h2>
                        <p>Price: ${product.price}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ProductList;
