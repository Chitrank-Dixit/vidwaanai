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

### Verse 1 (Vishnu Puran 0.3541)
- **Original**: 9 तथैव प्रहसंस्थान॑ प्रमाणानि यथा तथा। समाचक्ष् महाभाग तन्‍्महां परिपृष्छते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3542)
- **Original**: 2 श्रीपराशर उवाच रबिचन्धमसोर्यावन्‍्मयूखैरवभास्यते । ससमुद्रसरिच्छैर्ता तावती पृथिव्री स्मृता। 3 यावद्ममाणा पृथ्चिवी विस्तारपरिमण्डलात्‌ । नभस्तावठामाणं वै व्यासमण्डलतो द्विज
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3543)
- **Original**: 4 भूमेयोंजनलक्षे तु सौरं मैत्रेय मण्डलम । लक्षाहिबाकरस्थापि मण्डल॑ शहिनः स्थितम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3544)
- **Original**: 5 पूर्ण शतसहस्रे तु योजनानां निशाकरात्‌। नक्षत्रमण्डल॑. कृत्ख्रमुपरिष्टात्काशते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3545)
- **Original**: 6 दे लक्षे चोत्तरे ब्रह्मन्‌ बुधो नक्षत्रमण्डलात्‌ । तावत्ममाणभागे तु बुधस्याप्युशना: स्थित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3546)
- **Original**: 7 अज्जारको5पि शुक्रस्य तठ्ममाणे व्यवस्थित: । लक्षद्ये तु भौमस्य स्थितो देवपुरोहित:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3547)
- **Original**: 8 शौरिशहस्पतेश्षोर्ध्व द्विलक्षे समबस्थितः । सप्तर्षिमण्डलं: तस्माल्लक्षमेके द्विजोत्तम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3548)
- **Original**: 9 ऋषिभ्यस्तु सहस्नाणां शतादूरध्व व्यवस्थित: । मेढीभूतः समस्तस्य ज्योतिश्रक्रस्य वै ध्रुवः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3549)
- **Original**: 90 तैलोक्यमेतत्कथितमुत्सेपेन. महामुने । कुज्याफलस्य भूरेषा दृण्या चात्र प्रतिष्ठिता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3550)
- **Original**: 19 धुवादूध्व॑ महलोंकों यत्र ते कल्पवासिनः । एकयोजनकोटिस्तु यत्र ते कल्पबासिनः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3551)
- **Original**: 12 दे कोटी तु जनो लोको यत्र ते ब्रह्मण: सुता: । सनन्दनाशाः प्रथिता मैश्रेयामलखेतसः ।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3552)
- **Original**: 13 चतुर्गुणोत्तरे चोध्व जनलोकात्तप: स्थितम्‌। बैराजा यत्र ते देवा: स्थिता दाहविवर्जिता:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3553)
- **Original**: 94 अ्रीमैश्रेयजी खोले--बरह्मन्‌ ! आपने मुझसे समस्त भूमण्डलका वर्णन किया। है मुने ! अब मैं भुवर्लॉक आदि समस्त लोकोंके विषयमें सुनना चाहता हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3554)
- **Original**: हे महाभाग ! मुझ जिज्ञासुसे आप अहगंणकी स्थिति तथा उनके परिमाण आदिका यथाबत्‌ वर्णन कीजिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3555)
- **Original**: श्रीपराशरजी बोले--जितनी दूरतक सूर्य और चत्रमाकी किरणोंका प्रकाश जाता है; समुद्र, नदी और पर्वतादिसे युक्त उतना प्रदेश पृथिंवी कहलाता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3556)
- **Original**: हे द्विज ! जितना पृथिवीका विस्तार और परिमण्डल (घेरा) है ठतना ही विस्तार और परिमप्डक भुवर्ोकका भी है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3557)
- **Original**: हे मैत्रेय ! पृथिबीसे एक छाख योजन दूर सूर्यमण्डल है और सूर्यमण्डलसे भी एक रूक्ष योजनके अच्तरपर चन्द्रमण्डल है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3558)
- **Original**: चन्द्रमासे पुरे सौ हजार (एक स्तख) योजन ऊपर सप्पूर्ण नक्षत्रमण्डल प्रकाशित हो रहा है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3559)
- **Original**: हे ब्रह्मन्‌ ! नक्षत्रमण्डलूसे दो स्मसख योजन ऊपर बुध और बुधसे भी दो लक्ष योजन ऊपर शुक्र स्थित हैं । 7
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3560)
- **Original**: शुक्रसे इतनी ही दूरीपर मंगल हैं और मंगलसे भी दो लाख योजन ऊपर बृहस्पतिजी हैं।8
- **Translation**: 

---

