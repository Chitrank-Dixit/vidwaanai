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

### Verse 1 (Vishnu Puran 0.10461)
- **Original**: बलरामजीने उसके मस्तकपर घुँसोंसे तथा वक्षःस्थलमें जानुसे प्रहार किया और उस गतायु दैत्यको पूृथिवीपर पटककर रौंद डाला
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10462)
- **Original**: तदनत्तर श्रीकृष्णचन्द्रने महाबली मल्लराज तोशलको यायें हाथसे घूँसा मारकर पृथिजीपर गिरा दिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10463)
- **Original**: मल्लझ्ेष्ठ चाणूर और मुष्टिकके मारे जानेपर तथा मल्लराज तोशलके नष्ट होनेपर समस्त मल्लगण भाग गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10464)
- **Original**: तब कृष्ण और संकर्षण अपने समवयस्क गोपोफों बलपूर्वक खींचकर [ आलिंगन करते हुए ] हर्षसे रंगभूमिमें उछलने रंगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10465)
- **Original**: 3898 कंसो5पि कोपरक्ताक्ष: प्राहोशैव्यायतात्ररान्‌ श्रीविष्णुपुराण [ आ« 20 तदनन्तर कंसने क्रोधसे नेत्र छाल करके वज्नाँ एकब्रित गोपावेतौ समाजौधान्निष्क्राम्येतां बलादित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10466)
- **Original**: हुए. पुरुषोंसे कहा--'“ओरे ! इस समाजसे इन नन्दो5षपि गृह्मातां पापों निर्गलैरायसैरिह । अवृद्धाेण दण्डेन बसुदेब्रोडईपि वध्यताम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10467)
- **Original**: 83 वल्गन्ति गोपा: कृष्णेन ये चेमे सहिता: पुरः । गावो निगृह्ातामेषां यज्चास्ति वस्तु किल्नन
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10468)
- **Original**: 84 एबमाज्ञापयन्त॑ तु प्रहस्थमथुसूदन: । उत्पुत्यारुद्या त॑ मझ्ल॑ कंस जग्राह वेगत:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10469)
- **Original**: 85 केशेप्लाकृष्ष.. विगलत्किरीटमवनीतले । स कंस पातयामास तस्योपरि पपात चर
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10470)
- **Original**: 86 अश्लेषजगदाधारगुरुणा पततोपरि । कुष्णेन त्याजितः ग्राणानुग्रसेनात्मजो नृप:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10471)
- **Original**: 87 मृतस्थ केशेषु तदा गृहीत्वा मधुसूदन:। चकर्ष देहं कंसस्य रक़मध्ये महाबल:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10472)
- **Original**: 88 गौरवेणातिपहता परिधा तेन कृष्यता । कृता कंसस्य देहेन वेगेनेब महाम्मस:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10473)
- **Original**: 89 कंसे गृहीते कृष्णेन तद्भ्राताउभ्यागतो रुघा । सुमाली बलभद्रेण लील्यैव निपातित:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10474)
- **Original**: 90 त्तो हाहाकृत॑ सर्वमासीत्तद्गइमण्डलम्‌ अवज़या हत॑ दृष्ठा कृष्णेन मथुरेश्वरम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10475)
- **Original**: 91 कृष्णो5पि वसुदेवस्थ पादौ जग्राह सत्वरः । देवक्याश्र॒ महाबाहुर्बल्देवसहायबान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10476)
- **Original**: 92 उत्धाप्य बसुदेवस्तं देवकी च जनार्दनम्‌। स्पृतजन्मोक्ततचनौ तावेव प्रणतौ स्थितों
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10477)
- **Original**: 93 श्रीवसुद्देव उवाच अ्रसीद सीदतां दत्तो देवानां यो वरः प्रभो तथावयो: प्रसादेन कृतोद्धारस्स केशव
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10478)
- **Original**: 94 आराधितों यद्धणवानवतीणों गृहे मम। दुर्वृत॒निधनार्थाय तेन नः पावितं कुलम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10479)
- **Original**: 95 स्वमन्तः सर्वभूतानां सर्वभूतमयः स्थित: । अबर्तेते समस्तात्मस्वत्तो भूतभविष्यती
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10480)
- **Original**: 96 ग्वाल््याल्लेंकी बलपूर्वक निकाल दो
- **Translation**: 

---

