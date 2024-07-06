#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, request, jsonify
app = Flask(__name__)
import pickle


# In[8]:




model = pickle.load(open('mobile_price.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    output = prediction[0]
    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# In[ ]:




