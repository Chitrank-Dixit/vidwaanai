# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Bramha 0.5461)
- **Original**: समुद्रपर्यन्त पृथ्वीका ग्यारह हजार वर्षोतक पालन हर लिया और लड्ढ् नगरीमें लाकर रखा। फिर
- **Translation**: 

---

### Verse 2 (Bramha 0.5462)
- **Original**: किया। उसके बाद वे अपने वैष्णव धाममें प्रवेश सीताके लिये मोहित होकर उसने उनको भी हर
- **Translation**: 

---

### Verse 3 (Bramha 0.5463)
- **Original**: कर गये। ठस समय श्रीरामने वह प्रतिमा समुद्रको लानेका प्रयत्न किया। श्रीरामके सम्मुख जानेमें
- **Translation**: 

---

### Verse 4 (Bramha 0.5464)
- **Original**: दे दी और कहा-“अपने जल और र्ञोंके साथ उसे भय होता था; इसलिये मारीचको सुवर्णमय
- **Translation**: 

---

### Verse 5 (Bramha 0.5465)
- **Original**: तुम इस प्रतिमाकी भी रक्षा करना।' मृगके रूपमें भेजकर उन्हें आश्रमसे दूर हटा दिया
- **Translation**: 

---

### Verse 6 (Bramha 0.5466)
- **Original**: . ट्वापर आनेपर जब जगदीश्वर भगवान्‌ विष्णु और सीताकों अकेली पाकर हर लिया। इसका ! पृथ्वीकी प्रार्थनासे कंस आदिका बध करनेके पता लगनेपर लक्ष्मणसहित श्रीरामको बड़ा क्रोध
- **Translation**: 

---

### Verse 7 (Bramha 0.5467)
- **Original**: लिये बलभद्रजीके साथ वसुदेवजीके कुलमें अवतीर्ण हुआ। उन्होंने रावणको मार डालनेका निश्चय
- **Translation**: 

---

### Verse 8 (Bramha 0.5468)
- **Original**: हुए, उस समय नदियोंके स्वामी समुद्रने उस परम किया। इस कार्यमें सुग्रीव सहायक हुए। सुप्रीयका
- **Translation**: 

---

### Verse 9 (Bramha 0.5469)
- **Original**: दुर्लभ पुण्यमय पुरुषोत्तमक्षेत्रमें सम्पूर्ण लोकोंका वालीके साथ बैर था, अतः श्रीरामने बालीको
- **Translation**: 

---

### Verse 10 (Bramha 0.5470)
- **Original**: हित करनेके लिये उक्त प्रतिमाकों प्रकट किया, पारकर सुग्रीवको किष्किन्धाके राज्यपर अभिषिक्त
- **Translation**: 

---

### Verse 11 (Bramha 0.5471)
- **Original**: जो सम्पूर्ण मनोबाब्छित फलोंको देनेबाली थी। कर दिया और अज्गभदकों युवराज बनाया। फिर
- **Translation**: 

---

### Verse 12 (Bramha 0.5472)
- **Original**: तबसे उस मुक्तिदायक क्षेत्रमें हो देवाधिदेव अनन्त हनुमानू, नल, नील, जाम्बवानू, पनस, गबय,
- **Translation**: 

---

### Verse 13 (Bramha 0.5473)
- **Original**: वासुदेव विराजमान हैं, जो मनुष्योंकी समस्त गवाक्ष और पाठौीन आदि असंख्य महाबली
- **Translation**: 

---

### Verse 14 (Bramha 0.5474)
- **Original**: कामनाएँ पूर्ण करनेवाले हैं। जो लोग मन, वाणी बानरोंके साथ कमलनयन श्रीरामने लड्जकी यात्रा ' और क्रियाद्वारा सदा सर्वेश्वर भगवान्‌ अनन्त की । उन्होंने समुद्रमें पर्वतोंकी बड़ी-बड़ी च॒ट्टानें
- **Translation**: 

---

### Verse 15 (Bramha 0.5475)
- **Original**: वासुदेवकी भक्तिपूर्वक शरण लेते हैं, वे परमपदको डालकर पुल बँधाया और विशाल सेनाके साथ
- **Translation**: 

---

### Verse 16 (Bramha 0.5476)
- **Original**: प्राप्त होते हैं। भगवान्‌ अनन्तका एक बार दर्शन, समुद्रकों पार किया। रावणने राक्षसोंकों साथ
- **Translation**: 

---

### Verse 17 (Bramha 0.5477)
- **Original**: भक्तिपूर्वकक पूजन और प्रणाम करके मनुष्य लेकर भगवान्‌ श्रीरामके साथ घोर संग्राम किया।
- **Translation**: 

---

### Verse 18 (Bramha 0.5478)
- **Original**: राजसूय और अश्वमेध-यज्ञोंसे दसगुना फल पाता परम पराक्रमी श्रीरघुनाथजीने महोदर, प्रहस्त,
- **Translation**: 

---

### Verse 19 (Bramha 0.5479)
- **Original**: है। बह समस्त भोग-सामग्रीसे सम्पन्न छोटी- निकुम्भ, कुम्भ, नरान्तक, यमान्तक, मालाढ्य,
- **Translation**: 

---

### Verse 20 (Bramha 0.5480)
- **Original**: छोटी घंटियोंसे सुशोभित, सूर्यके समान तेजस्वी माल्यवान्‌ू, इन्द्रजित्‌, कुम्भकर्ण तथा रावणकों
- **Translation**: 

---

