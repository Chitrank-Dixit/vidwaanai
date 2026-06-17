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

### Verse 1 (Vishnu Puran 0.3601)
- **Original**: 128 श्रीविष्णुपुराण [ आ0 7 तयो: सैब पृथर्मावकारणं संश्रयस्थ च । है ! महामते ! वह विष्णु-शक्ति ही [प्रछयके समय] क्षोभकारणभूता च सर्गकाले महामते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3602)
- **Original**: उनके पार्थक्य और (स्थितिके समय] उनके सम्मिलनको यथा सक्ते जले बातो ब्रिभत्ति कणिकाशतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3603)
- **Original**: शक्ति: सापि तथा विष्णो: प्रधानपुरुषात्मकम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3604)
- **Original**: 31 यथा च पादपो मूलस्कन्धज्ञाखादिसंयुत: । आदिबीजात्रभवति बीजान्यन्यानि वै तत:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3605)
- **Original**: 32 प्रभवन्ति ततस्तेभ्य: सम्भवन्त्यपरे द्रमा: । तेअपि तलल्‍लक्षणद्रव्यकारणानुगता मुने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3606)
- **Original**: 33 एवमव्याकृतात्पू्व. जायन्ते महदादयः । विदेषान्तास्ततस्तेभ्य: सम्भक्ल्यसुरादयः । तेभ्यश्न पुन्रास्तेषां च॒ पुत्राणामपरे सुताः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3607)
- **Original**: 34 बीजाइृक्षप्ररोहेण यथा नापचयस्तरो: । भूतानां भूत्सर्गेण नैवास्त्थपच्यस्तथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3608)
- **Original**: 35 सन्निधानाद्यथाकाशकालाद्या: कारणं तरो: । तथैवापरिणामेन विश्वस्थ भगवान्हरि:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3609)
- **Original**: 36 ब्रीहिबीजे यथा मूल नाल पत्राडुरौ तथा । काण्ड कोषस्तु पुष्प॑ च क्षीरं तद्बद्च तण्डुला:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3610)
- **Original**: 37 तुषा: कणाश् सन्तो वै यात्त्याविर्भावमात्मन: । प्ररोहहेतुसामग्रीमासाह्य मुनिसत्तम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3611)
- **Original**: 38 तथा कर्मस्वनेकेषु देवाद्या: सम्रवस्थिता: । विष्णुशक्ति समासाद्य प्ररोहमुपयान्ति वै
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3612)
- **Original**: 39 सच विष्णु: पर॑ ब्रह्म यतः सर्व॒मिदं जगत्‌ । जगन्च यो यत्र चेद यर्मिश् लयमेष्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3613)
- **Original**: 40 तद्ढह्मा तत्पर धाम सदसत्परम॑ पदम्‌ । यस्थ सर्वप्भेदेन यतशैतघराचरम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3614)
- **Original**: 49 स एब मूलप्रकृतिरव््यक्तरूपी जगच्च सः । तस्मिन्नेब लय सर्वे याति तत्र च॒ तिप्ठति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3615)
- **Original**: 42 कर्ताक्रियाणां सच इज्यते क्रतुः . स॒ एवं तत्कर्मफ्े च तस्य। खुगादि यत्साधनमप्यशेष...... हेतु है तथा सर्गास्ण्यके समय वही उनके क्षोभकी कारण है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3616)
- **Original**: जिस प्रकार जलके संसर्गसे वायु सैकड़ों जल- कणोंको धारण करता है ठसी प्रकार भगवान्‌ विष्णुकी दाक्ति भी प्रधान-पुरुषमय जगत्‌को धारण करती है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3617)
- **Original**: है मुने ! जिस प्रकार आदि-बीजसे ही मूल, स्कन्ध तदनन्तर उससे और भी बीज उत्पन्न होते हैं, तथा उन बीजोंसे आन्यान्य वृक्ष उत्पत्र होते हैं और ले भी उन्हीं लक्षण, द्रब्य और कारणोंसे युक्त होते हैं, उसी प्रकार पहले अव्याकृत (प्रधान) से महत्तत्व्से लेकर पत्नभूतपर्यन्त [सप्पूर्ण विकार] उत्पन्न होते हैं तथा उनसे देव, असुर आदिका जन्म होता है और फिर उनके पुत्र तथा उन पुत्रोंके अन्य पुत्र होते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3618)
- **Original**: 32--34
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3619)
- **Original**: अपने बीजसे अन्य वक्षके उत्पन्न बोनेसे जिस प्रकार पूर्ववुक्षकी कोई क्षति नहीं होती डसी प्रकार अन्य प्राणियोंके उत्पन्न होनेसे उनके जन्मदाता प्राणियोंका दास नहीं होता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3620)
- **Original**: जिस प्रकार आकादा और काल आदि सपच्निधिमात्रसे हो वृक्षके कारण होते हैं उसी प्रकार भगवान्‌ ओहरि भी बिना परिणामदे; ही विश्वके कारण हैं
- **Translation**: 

---

