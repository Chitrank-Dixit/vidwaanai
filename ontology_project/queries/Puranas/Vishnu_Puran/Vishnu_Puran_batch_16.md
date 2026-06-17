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

### Verse 1 (Vishnu Puran 0.301)
- **Original**: श्रीयरूभद्रजी भी अपमे भुजदप्ड्ोको ठोकते हुए अति मनोहर भावसे उछलने लगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.302)
- **Original**: उस समय उनके पद-पदपर पृथिबी नहीं फटी, यही चड़ा आश्चर्य है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.303)
- **Original**: तदनत्तर अमित-चविक्रम कृष्णचच्द्र चाणूरके साथ और इन्द्रयुद्धकुल राश्षस मुष्टिक खलभद्रके साथ युद्ध करने लगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.304)
- **Original**: कृष्णचन्द्र चाणूरके साथ परस्पर भिड़कर,
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.305)
- **Original**: हरे आंकष्णुपुराण [ अण्ड भवतो यत्परं तत्त्व तज्न जानाति कश्नन । अवतारेषु यद्प॑तदचन्ति दिवोकस:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.306)
- **Original**: 17 त्वामाराध्य पर ब्रह्म याता मुर्क्ति मुमुक्षव: । वासुदेवमनाराध्य को मोक्ष समवाप्स्यति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.307)
- **Original**: 98 काका फनपकस पक करा महू मन आह्वां यदप्राहां ;। बुद्धणा च तद॒पमखिलंं तव
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.308)
- **Original**: 19 त्वन्ययाह त्वदाधारा त्वत्सूष्टा त्वत्समाश्रया । माधवीमिति स्त्रेकोडयमभिधत्ते ततो हि माम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.309)
- **Original**: 20 जयाखिलज्ञानमय जय स्थूलमयाव्यय । जयाउनन्त जयाव्यक्त जय व्यक्तमय प्रभो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.310)
- **Original**: 21 परापरात्मन्विश्वात्मक्षयआ. यज्ञपतेउनघ । त्व॑ अज्ञस्त्वं बघदकारस्त्वमोड्भररस्त्वमञ्मय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.311)
- **Original**: 22 लव बेदास्त्व॑ तदड़ानि त्व॑ यज्ञपुरुषों हरे। सूर्चाद्यो ग्रहास्तारा नक्षत्राण्यसिलं जगत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.312)
- **Original**: 23 अफमदुसयी बकरे पक जर दृष्य॑ चल पुरुषोत्तम । यज्च के मयात्र परमेश्वर । तत्सईव॑ त्वे नमस्तुभ्य भूयों भूयो नमो नमः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.313)
- **Original**: 24 श्रीपााशर उवाच एवं संस्तृयमानस्तु पृथिव्या धरणीध्रः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.314)
- **Original**: सामस्वरध्वनि: श्रीमा्लगर्ज परिघर्घरम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.315)
- **Original**: 25 तत: समुस्क्षिप्प धरां स्वदंष्टया महावराह: स्फुटपदल्प्रेचन: । रसातलादुत्पलपत्रसन्निभ: समुत्यितो नील इवाचलो महान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.316)
- **Original**: 26 उत्तिष्ठठा तेन मुखानिलाहतं ; तत्सम्भवाम्भो जनलोकसंप्रयान्‌ । प्रक्षालयामास हि तान्महाञ्युतीन्‌ सनन्दनादीनपकल्मषान्‌ मुनीन्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.317)
- **Original**: 27 प्रयान्ति तोयानि खुराग्रविक्षत- रसातले5धथ: कृतशब्दसन्तति । शध्वासानिलास्ता: परितः प्रयान्ति सिद्धा जने ये नियता बसन्ति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.318)
- **Original**: 28 है गोबजिन्द
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.319)
- **Original**: सबको भक्षणकर अन्तमें आप ही मनीषिजनोंद्राण चिन्तित होते हुए जलमें शायन करते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.320)
- **Original**: है प्रभो ! आपका जो परतत्त्व है उसे तो कोई श्री गहीं जानता; अत: आपका जो रूप अवतारोंगें प्रकट होता है उसीकी देवगण पूजा करते हैं
- **Translation**: 

---

