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

### Verse 1 (Vishnu Puran 0.8781)
- **Original**: तस्थानु यस्तस्थ कर्थ ममत्व... हद्यास्पद॑मत्यभवव॑ करोति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8782)
- **Original**: 135 3-06 किला ममैषाशु परित्यजैनां खदन्ति ये दूतमुखेस्तवशबरूत्‌। नराधिपास्तेषु_ ममातिहासः ... प़ुनश्चमूकेषु दयाभ्युपैति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8783)
- **Original**: 136 श्रीपरादार उवाच इत्येते धरणीगीताइइलोका मैत्रेय यैज्श्रुता: । ममत्व विछर्य॑ याति तपत्यर्के यथा हिपम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8784)
- **Original**: 137 इत्पेष कथितः सम्यद्भुनोर्वशो मया तल । यत्र स्थितप्रवृत्तस्थ विष्णोरंशांशका नृपा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8785)
- **Original**: 138 श्रूणोति य इम॑ भक्त्या मनोर्वशमनुक्रमात्‌ । तस्य पापमशेषं वे प्रणश्यत्यमलात्मन:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8786)
- **Original**: 139 पृथिवी कहती है--अहो ! बुद्धिमान्‌ होते हुए भो इन राजाओऑँंको यह कैसा मोह हो रहा है जिसके कारण ये बुल्तबुलेके समान क्षणस्थायी होते हुए भी अपनी स्थिरतामें इतना विश्वास रखते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8787)
- **Original**: ये त्ेग प्रथम अपनेकों जीतते हैं और फिर अपने मच्नियोंकों तथा इसके अनन्तर ये क्रमञः अपने भृत्य, पुरनासी एबं शजुओंक्े जीतना चाहते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8788)
- **Original**: “इसी क्रमसे हम समुद्रपर्यन्त इस सम्पूर्ण पृथिवीक्त्रे जीत छेंगे' ऐसी बुद्धिसे मोहित हुए ये वेग अपनी निकटवर्तिनी मृत्युको नहीं देखते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8789)
- **Original**: यदि सपुद्रसे घिय हुआ यह सम्पूर्ण भूमण्डल अपने बढ़ामें हो ही जाय तो भी मनोजयकी अपेक्षा इसका मूल्य ही क्या है ? क्योंकि मोक्ष तो मनोजयसे ही प्राप्त होता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8790)
- **Original**: जिसे छोड़कर इनके पूर्वज चले गये तथा जिसे अपने साथ केकर इनके पिता भी नहीं गये उसी मुझको अत्यन्त मूर्खताके कारण ये राजालोग जौतना चाहते हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8791)
- **Original**: जिनका चित ममतामय है उन पिता-पुत्र और भाइयोमें अत्यन्त मोहके कारण मेरे ही लिये परस्पर कलह होता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8792)
- **Original**: जो-जे राजालोग यहाँ हो चुके हैं उन सभीकरो ऐसी कुबुद्धि रही है कि यह सम्पूर्ण पृथिवी मेरी ही है ओर मेरे पीछे यह सदा मेरी सन्तानकी हीं रहेगी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8793)
- **Original**: इस प्रकार मेरेमें ममता करनेवाले एक राजाको, मुझे छोड़कर मृत्युके मुखमें जाते हुए देखकर भी न जाने कैसे उसका उत्तराधिकारी अपने हृदयमें मेरे ल्थिये ममताको स्थान देता है ?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8794)
- **Original**: जो राजास््रेग टूतोंकि ड्रास अपने झत्नरुओंसे इस प्रकार कहत्वते हैं कि “यह पृथिल्री मेरी है तुमछोग इसे तुरन्त छोड़कर चले जाओ' उनपर मुझे बड़ी हँसी आती है और फिर उन मूढॉपर मुझे दया भी आ जाती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8795)
- **Original**: श्रीपरादारजी खोल्े--है सैत्रेय ! पृधिवौके कहे हृए. इन इल्म्रेकॉक्ये जो पुरुष सनेगा उसकी ममता इसी प्रकार ल्लीन हो जायगी जैसे सूर्यके तपते समय बर्फ पिघलू जाता हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8796)
- **Original**: इस भ्रकार मैंने तुमसे भली प्रकार मनुके वेश्ञका वर्णन कर दिया जिस वेहके राजागण स्थितिकारक भगवान्‌ विष्णुके अंश-के-अंश थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8797)
- **Original**: जो पुरुष इस मनुवेज्षका क्रमशः श्रवण करता है उस शुद्धात्माके सस्पूर्ण पाप नष्ट हो जाते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8798)
- **Original**: चतुर्थ अंडा 305 श्रुत्वैवमखिलं ब॑झं प्रद्मस्तं शशिसूर्ययो:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8799)
- **Original**: 140 इश्न्बाकुजह्ुमान्थातृसगराविश्षितात्रघून्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8800)
- **Original**: ययातिनहुषाद्यांश्ष ज्ञात्वा निष्ठामुपागतान्‌
- **Translation**: 

---

