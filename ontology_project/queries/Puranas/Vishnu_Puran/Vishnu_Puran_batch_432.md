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

### Verse 1 (Vishnu Puran 0.8621)
- **Original**: ततप्योडश शका भूषतयो. भवितार:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8622)
- **Original**: ततश्चाषप्टो यवनाश्तुर्दश तुरुष्कारा मुण्डाश्न त्रयोदश एकादश मौना एते वै पृथिवीपतय: पृथिवरीं दशवर्षशतानि नवत्यधिकानि भोक्ष्यन्ति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8623)
- **Original**: ततश्ल एकादश भूषतयोउब्दह्वतानि त्रीणि पृथिवीं भोक्ष्यन्ति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8624)
- **Original**: तेपूत्सत्रेषु कैड्डित्त यवना भूपतयो भविष्यन्त्यमूर्डाभिषिक्ता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8625)
- **Original**: चतुर्थ अदा 299 भागवत और भागवतका पुत्र देवभूत होगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8626)
- **Original**: ये झुंगगरेश एक सौ बारह वर्ष पृश्चितीका भोग करेंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8627)
- **Original**: इसके अनन्तर यह पृथिवों कण्व भूृपाल्फेके अधिकारमें चली जायगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8628)
- **Original**: शझ्ुुंगवंशीय अति ज्यसनशील राजा देवभूतिको कण्बवंशीय वसुदेत नामक उसका मन्‍्ज़ी मारकर स्वये राज्य भोगेगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8629)
- **Original**: उसका पुत्र भूमित्र, भूमित्रकाा नारायण तथा नारायणका पुत्र सुदार्मा होगा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8630)
- **Original**: ये चार काण्व भूषतिगण पैंतालीस वर्ष पृथिवीके अधिपति रहेंगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8631)
- **Original**: कण्ववंशीय सुशर्माको उसका बलिपुच्छक नामवाल्ा आखजातीय सेवक मारकर स्वयं पृथिवॉका भोग करेगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8632)
- **Original**: उसके पीछे उसका भाई कृष्ण पृथिवोका स्वामी होगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8633)
- **Original**: उसका पुत्र शान्तकर्णि होगा। झञान्तकर्णिका पूत्र पूर्णोत्संग, पूर्णोस्सेगक्रा शातकर्णि, शातकर्णिका ल्म्बोदर, लम्बोदरका पिलूक, पिल्करका मेघस्वाति, मेघस्वातिका पटुमान्‌, पटुमानका अरिष्टकर्मा, अरिप्रकर्माका हाल्त्रहऊ,. हाल्रहऊका पलक, पललकक्ा पुलिन्दसेन, पुलिन्दसेनका सुन्दर, सुन्दरका ज्ातकर्णि,
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8634)
- **Original**: शातकर्णिका शदियस्थाति, जिवस्वातिका गोमतिपुत्र, गोमतिपुत्रका अलल्‍्मान्‌, अलिमानूका शात्तकर्णि [ दूसरा ], शान्तकर्णिका यज्ञश्रीका द्वियज्ञ, द्वियज्ञका क्‍न्‍द्रश्रो तथा चन्द्रश्नीका पुत्र पुलोमाचि होगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8635)
- **Original**: 45--49
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8636)
- **Original**: इस प्रकार ये तीस आखभृत्य राजागण चार सौ छप्पन वर्ष पृथिबीको भोगेंगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8637)
- **Original**: इनके पीछे सात आभीर और दस गर्दभिल राजा होंगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8638)
- **Original**: फिर सोलह शक राजा होंगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8639)
- **Original**: उनके पीछे आठ यवन, चौदह तुर्क, तेरह मुण्ड (गुरुण्ड) और ग्यारह मौनजातीय- राजाल्केग एक हजार नब्बे खर्ष प्रथिवीका दासन करेंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8640)
- **Original**: इनमेंसे भी म्यारट मौन राजा पृथिबीक्ले तीन सौ यर्षतक भोगेंगे
- **Translation**: 

---

