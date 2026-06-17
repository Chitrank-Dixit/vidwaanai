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

### Verse 1 (Vishnu Puran 0.12801)
- **Original**: हे नरेश ! भगवान्‌का वही रूप अपनी स्जैल्मसे देव, तिर्यक्‌ और मनुष्यादिकी चेष्टाओंसे युक्त सर्वशक्तिमय रूप घारण करता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12802)
- **Original**: इन रूपॉमें अप्रमेय भगवान्‌की जो व्यापक एवं अव्याहत चेष्टा होती है वह संसारके उपकारके ल्लये ही होती है, कर्मजन्य नहीं होती
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12803)
- **Original**: है राजन्‌ ! योगाभ्यासीको आत्म-शुद्धिके लिये भगवान्‌ विश्वरूपके उस सर्वपापनाशक रूफका ही चिन्तन करना चाहिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12804)
- **Original**: जिस प्रकार वायुसहित अप्मनि ऊँची ज्वाल्मऑसे युक्त होकर शुष्क तृणसमृहकों जल्म डालता है उसी प्रकार चित्तमें रिथत हुए भगबान्‌ विष्णु योगियोंके समस्त पाप नष्ट कर देते है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12805)
- **Original**: इसलिये सम्पूर्ण शाक्तियोंके आधार भगवान्‌ विष्णुमें चित्तको स्थिर करे, यही शुद्ध धारणा है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12806)
- **Original**: है राजन्‌ ! तीनों भावनाओंसे अतोत भगवान्‌ विष्णु हो योगिजनोंकी मक्तिके लिये उनके [ स्वतः ] चशल तथा [ किसी अनूठे विषयमें ] स्थिर रहनेवाले चित्तके शुभ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12807)
- **Original**: 452 श्रीविष्णुपुराण [ अ0 7 अन्ये तु पुरुषव्याप्र चेतसो ये व्यपाश्रयाः । अशुद्धास्ते समस्तास्तु देवाद्या: कर्मयोनय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12808)
- **Original**: 77 मूर्त्त भगबतो रूप सर्वापाश्रयनिःस्पृहम्‌ । एपा वै धारणा प्रोक्ता यघित्तं तत्र धार्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12809)
- **Original**: 78 यद्व मूर्त हरे रूप॑ यादृक्किन्त्य नराधिप । तच्छूबतामनाधारा धारणा नोपपछाते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12810)
- **Original**: 79 प्रसन्नवदर्न चारुपद्मपन्नोपमेक्षणम्‌ । सुकपोलं सुबिस्तीर्णललाटफलकोम्ज्वलम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12811)
- **Original**: 80 समकर्णान्तविन्यस्तचारुकुण्डलभूषणम्‌ । कम्बुप्रीब॑ सुविस्तीर्णश्रीवत्साड्धितवक्षसम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12812)
- **Original**: 81 बलिब्रिभड्िना मग्ननाभिना हुदरेण च। प्रलूम्बाष्टभुजं॑ विष्णुमथवापि चतुर्भुजम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12813)
- **Original**: 82 समस्थितोरुजजूं च सुस्थिताडूप्रिवराम्बुजम्‌ । चिन्तयेद्ृह्म भूत, ते पीतनिर्मछवाससम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12814)
- **Original**: 83 किरीटहारकेयूरकटकादिविभूषितम्‌_
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12815)
- **Original**: 84 शार्ईशब्बगदाखड्गचक्रा क्षबलयान्वितम्‌ । वरदाभयहस्त॑ च्॒ मुद्रिकारत्रभूषितम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12816)
- **Original**: 85 चिन्तयेत्तन्ययो योगी समाधाबात्ममानसम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12817)
- **Original**: तावश्लावददुढीभूता तत्रैव नृप धारणा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12818)
- **Original**: 86 म्रजतस्तिष्ठतोन्यद्धा स्वेच्छया कर्म कुर्वतः । नापयाति यदा चित्तात्सिद्धां मन्येत ता तदा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12819)
- **Original**: 87 तत: शद्घुगदाच्क्रशा्ड्रीदिरहित॑ बुधः । चिन्तयेद्धगवद्गुपं॑ प्रशान्त॑ साक्षसूत्रकम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12820)
- **Original**: 88 सा यदा धारणा तद्गदबस्थानवती ततः। किरीटकेयूरमुखैर्भूषणे रहिते. स्मरेत्‌
- **Translation**: 

---

