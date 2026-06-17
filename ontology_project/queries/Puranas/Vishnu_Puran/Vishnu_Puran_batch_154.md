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

### Verse 1 (Vishnu Puran 0.3061)
- **Original**: उनके रससे निकली जम्बू नामकी प्रसिद्ध नदी वहाँ खहती है, जिसका जरः वहाँकि रहनेवाले पीते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3062)
- **Original**: उसका पान करनेसे वहाँके शुद्धाचित्त छोगोंक्रों पसीना, दुर्ग, बुढ़ापा अथवा इन्द्रियक्षय नहीं होता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3063)
- **Original**: उसके क्िनारेकी मृत्तिका उस स्ससे मिरकर मन्द-मन्द वायुसे सूखनेपर जाम्बूनद नामक सुबर्ण हो जाती है, जो सिद्ध पुरुषोंका भूषण है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3064)
- **Original**: मेरुके पूर्वमें भद्राक्षयर्ष और पश्चिममें केतुमालवर्ष है तथा हे मुनिश्रेष्ठ ! इन दोनोंके
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3065)
- **Original**: 110 श्रीविष्णुपुराण (आः 2 बने चेत्ररथं पूर्वे दक्षिणे गन्धमादनम्‌। बैश्राज॑ पश्चिमे तददुत्ते नन्‍्दनं स्मृतम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3066)
- **Original**: 25 अरुणोदं॑ महाभद्रमसितोदं समानसम्‌ । सरांस्येतानि चत्वारि देवभोग्यानि सर्वदा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3067)
- **Original**: 26 ज्ीताम्भश्न कुमुन्द कुररी माल्यवांस्तथा । बैकड्भूअ्रमुखा मेरो: पूर्वतः केसराचला:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3068)
- **Original**: 27 त्रिकूट: झिशिसश्लैव पतड्ो रुचकस्तथा। निषदाद्या दक्षिणतस्तस्थ केसरपर्वता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3069)
- **Original**: 28 शिखिवासा: सबैडूर्य: कपिलो गन्धमादन: । जारुधिप्रमुस्वास्तद्वत्पक्षिमिे. केसराचला:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3070)
- **Original**: 29 मेरोरनत्तराष्ट्रेयु जठरादिषृवस्थिता: । शब्ब॒कूटोईथ ऋषभों हंसो नागस्तथापर: । कालझ्ाद्याश्न तथा उत्तरे केसराचलछा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3071)
- **Original**: 30 चतुर्दझसहस्नाणि योजनानां महापुरी । मेरोरुपरि मैत्रेय ब्रह्मण: प्रथिता दिवि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3072)
- **Original**: 31 तस्यास्समन्ततश्चाष्टो दिशासु विदिशासु च । इन्द्रादिलोकपालानां प्रख्याता: प्रवरा: पुर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3073)
- **Original**: 32 विष्णुपादविनिष्क्रात्ता प्रावयित्वेन्दुमण्डलम्‌ समन्ताद ब्रह्मण: पुर्या गड़ा पतति वै दिवः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3074)
- **Original**: 33 सा तत्र पतिता दिक्षु चतुर्द्धा प्रतिषद्यते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3075)
- **Original**: सीता चालकनन्दा च चक्षुभंद्रा च वै क्रमात्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3076)
- **Original**: 34 पूर्वेण झैलात्सीता तु दल यात्यन्तरिक्षगा । ततश्॒पूर्वनर्षेण भद्राश्वेनेति सार्णवम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3077)
- **Original**: 35 तथैबालकनन्दापि दक्षिणेनैत्य भारतम्‌ ज्रयाति सागर भूत्वा सप्तभेदा महामुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3078)
- **Original**: 36 चक्षुश्ष॒ पश्चिमगिरीनतीत्य सकल्ांस्ततः । पश्चिमं केतुमालाख्य॑ वर्ष गत्वैति सागरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3079)
- **Original**: 37 भद्रा तथोत्तरगिरीनुत्तरांश्य तथा कुझछन्‌। अतीत्योत्तरमम्भोधिं समभ्येति महामुने
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3080)
- **Original**: 38 आनीलनिषधायामौ माल्यवद््धमादनौ । तयोरम॑ध्यगतो मेरु: कर्णिकाकारसंस्थित:
- **Translation**: 

---

