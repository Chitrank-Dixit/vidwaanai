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

### Verse 1 (Vishnu Puran 0.5561)
- **Original**: संयमी और बुद्धिमान्‌ पुरुषोंक्रो इन समस्त पर्वदिनोंमें सच्छास्नायलोकन, देवोपासना, यश्ञानुष्ठान, ध्यात और जप आदियें लगे रहना चाहिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5562)
- **Original**: गौ-छ्मग आदि अन्य योनियोंसे, अयोनियोंसे, औषध-अयोगसे अथवा ब्राह्मण, देवता और गुरुके आश्रमॉमें कभी मैथुन न॑ करें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5563)
- **Original**: हे पृथिवीपते ! चैत्पवृक्षके नीचे, आँगनमें, तीर्थमें, पशुशाल्ममें, चौराहेपर, इमजानमें, उपबनमें अथवा जलमें भी मैथुन करना उचित नहीं है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5564)
- **Original**: हे राजन्‌! पूृलोक्त समस्त पर्वदिनोमें प्रातःकाकू और सा्यकालमें तथा मल-मूत्रके वेगके समय बुद्धिमान्‌ पुरुष मैथुनमें प्रवृत्तन हो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5565)
- **Original**: हे नृप ! पर्वदिनोमें स्रीगमन करनेसे धनकी हानि होती है; दिनमें करनेसे पाप होता है, पृथिवीपर करनेसे रोग होते हैं और जल्ाशयमें स्रीम्सब्र करनेसे अमंगल होता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5566)
- **Original**: परस्त्रीसे तो वाणीसे क्या, मनसे भी प्रसद्ग न करे, क्‍योंकि उनसे मैथुन करनेवालोक्रो अस्थि-बन्धन भो नहों होता [ अर्थात्‌ उन्हें अस्थिशृन्य कीटादि होना पड़ता है ? ).
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5567)
- **Original**: 200 [ अ* 12 मृतों नरकमभ्येति हीयतेउन्नापि चायुष: । परदाररतिः पुंसामिह चामुत्र भीतिदा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5568)
- **Original**: 126 इति मत्वा स्वदारेषु ऋतुमत्सु बुधो व्रजेत्‌ । यथोक्तदोषहीनेषु.. सकामेघ्चनृतावपि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5569)
- **Original**: 127 परस्त्रीकी आसक्ति पुरुषको इहल्म्रेक और परल्प्रेक दोनों जगह भय देनेवाली है; इहत्मेकमें उसकी आयु क्षोण हो जाती है और मरनेपर बह नरकमें जाता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5570)
- **Original**: ऐसा जानकर बुद्धिमान्‌ पुरुष उपरोक्त दोषोंसे रहित अपनी ख्रीसे ही ऋतुकालमें प्रसब्र करे तथा उसकी विद्येष अभिस्प्रषा हो तो बिना ऋतुकाल्के भी गमन करे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5571)
- **Original**: ख्णणननन जुडी पन्ना इति श्रीविष्णुपुणणे तृतीयेंउइशे एकादशो5उघ्याय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5572)
- **Original**: हि ह 3 ककममन्‍---न बारहवाँ अध्याय गृहस्थसम्बन्धी सदाचारका वर्णन आऔर्च उवाच देवगोब्राहणान्सिद्धान्वृद्धाचार्यास्तथार्चयेत्‌ । द्विकाछे चर नमेत्सन्थ्यामभीनुपचरेत्तथा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5573)
- **Original**: 1 सदा5नुपहते वस्त्रे प्रशस्ताश्ष महोषथी: । गारुड़ानि च रत्नानि बिभुयात्ययतों नरः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5574)
- **Original**: 2 अ्रस्रिग्धामलछकेशश्र सुगन्यश्चास्वेषधूक्‌ । सितास्सुमनसो हृद्या बरिभुयाश्ष नरस्सदा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5575)
- **Original**: 3 किख्िित्परस्व॑ न हरेन्नाल्यमप्यप्रिय॑ वदेत्‌ । प्रियं च्व नानृत॑ ब्रूयात्रान्यदोषानुदीरयेत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5576)
- **Original**: 4 नान्यरित्र्य॑ तथा खैरं रोचयेत्पुरुषर्षभ । न दुष्ट यानमारोहेल्कूलच्छायां न संश्रयेत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5577)
- **Original**: 5 विद्विप्टपतितोन्पत्तबहुवैरादिकीटकै जन्धकी वन्यकीभरतु: क्षुद्ावतकथैस्सह
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5578)
- **Original**: 6 तथातिव्ययशीलैश्ष. परिवादरतैइ्शठै: । बुधो मैत्री न कुर्वोत नैक: पन्धानमाश्रयेत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5579)
- **Original**: 7 नावगाहेजलौघस्थ वेगमग्ने.. नरेश्वर। अ्रदीप्त वेश्म न विशेन्नारोहेच्छिखरं तरो:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5580)
- **Original**: 8 न कुयहिन्तसड्ूर्ष कुष्णीयाश न नासिकाम्‌ नासंबृतमुखो जृम्मेच्छासकासौ विसर्जयेत्‌
- **Translation**: 

---

