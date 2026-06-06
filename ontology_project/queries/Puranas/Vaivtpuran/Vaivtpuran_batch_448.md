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

### Verse 1 (Vaivtpuran 23.1922)
- **Original**: ही पृथ्वी परम पावन बन गयी। तीर्थ स्वयं पवित्र सम्पूर्ण स्त्रियाँ इन्हींको रूप मानी जाती हैं। ये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1923)
- **Original**: होनेके लिये इनका दर्शन एवं स्पर्श करना चाहते पाँच देवियाँ परिपूर्णम कही गयो हैं। इन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1924)
- **Original**: हैं। इनके अभावमें अखिल जगतके सम्पूर्ण कर्म देवियोंके जो-जो प्रधान अंश हैं, अब उनका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1925)
- **Original**: निष्फल समझे जाते हैं। इनकी कृपासे मुमुक्षुजन वर्णन करता हूँ, सुनो। भूमण्डलकों पवित्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1926)
- **Original**: मुक्त हो जाते हैं। जो जिस कामनासे इनको करनेवाली गद्गा इनका प्रधान अंश हैं। ये
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1927)
- **Original**: उपासना करते हैं, उनको वे सारी इच्छाएँ पूर्ण सनातनी “गज्जा' जलमयी हैं। भगवान्‌ विष्णुके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1928)
- **Original**: हो जाती हैं। भारतवर्षमें वृक्षरूपसे पधारनेबाली बिग्रहसे इनका प्रादुर्भाव हुआ है। पापियोंके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1929)
- **Original**: ये देवी कल्पवृक्षस्वरूपा हैं। भारतवासियोंका पापमय ईंधनको भस्म करनेके लिये ये प्रज्वलित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1930)
- **Original**: त्राण (उद्धार एवं रक्षा) करनेके लिये इनका यहाँ अग्नि हैं। इन्हें स्पर्श करने, इनमें नहाने अथवा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1931)
- **Original**: पधारना हुआ है। ये पूजनीयोंमें परम देवता हैं। इनका जलपान करनेसे पुरुष कैवल्य-पदके प्रकृतिदेवीके एक अन्य प्रधान अंशका नाम अधिकारी हो जाते हैं। गोलोक-धाममें जानेके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1932)
- **Original**: देबी 'जरत्कारु' है। ये कश्यपजीकी मानसपुत्री लिये ये सुखप्रद सीढ़ीके रूपमें विराजमान हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1933)
- **Original**: हैं; अतः “मनसा' देवी कहलाती हैं। इन्हें भगवान्‌ इनका रूप परम पवित्र है। समस्त तीर्थों और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1934)
- **Original**: शंकरको प्रिय शिष्या होनेका सौभाग्य प्राप्त है। नदियोंमें ये श्रेष्ठ मानी जाती हैं। ये भगवान्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1935)
- **Original**: ये परम विदुषी हैं। नागराज शेषकी बहिन हैं। शंकरके मस्तकपर जटामें ठहरी थीं। बहाँसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1936)
- **Original**: सभी नाग इनका सम्मान करते हैं। नागकी निकलीं और पडूक्तिबद्ध होकर भारतवर्षमें आ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1937)
- **Original**: सवारीपर चलनेवाली इन अनुपम सुन्दरी देवीको गयौं। तपस्वीजन अपनी तपस्यामें सफलता प्राप्त [/नागेश्वरी' और “'नागमाता' भी कहा जाता है। कर सकें--एतदर्थ शीघ्र ही इनका पधारना हो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1938)
- **Original**: प्रधान-प्रधान नाग इनके साथ विराजमान रहते गया। इनका शुद्ध एवं सत्त्वमय स्वरूप चन्द्रमा,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1939)
- **Original**: हैं। ये नागोंसे सुशोभित रहती हैं। नागराज इनकी श्वेतकमल या दूधके समान स्वच्छ है। मल और [स्तुति करते हैं। ये सिद्धयोगिनी हैं और अहंकार इनमें लेशमात्र भी नहीं हैं। ये परम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1940)
- **Original**: नागलोकमें निवास करती हैं। ये विष्णुस्वरूपिणी साध्वी गड्डा भगवान्‌ नारायणको बहुत प्रिय हैं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1941)
- **Original**: हैं। भगवान्‌ विष्णुमें इनकी अटल श्रद्धा-भक्ति श्री 'तुलसी' को प्रकृतिदेवीका प्रधान
- **Translation**: 

---

