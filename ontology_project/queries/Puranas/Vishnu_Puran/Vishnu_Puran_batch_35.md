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

### Verse 1 (Vishnu Puran 0.681)
- **Original**: 33 बेदना स्वसु्त चापि दुःख जज्े5थ रौरबात्‌। मृत्योव्याधिजराशोकतृष्णाक्रोधाश् जज्ञिरे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.682)
- **Original**: 34 दुःस्वोत्तरा: स्पृता होते सर्वे चाथर्मलूक्षणा: । नैषां पुत्रोउस्ति वै भार्या ते सर्विे ह्यूध्वरितस:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.683)
- **Original**: 35 रौद्राण्येतानि रूपाणि विष्णोर्मुनिवरात्मज । नित्यप्रलयहेतुत्व॑जगतोउस्य प्रयान्ति वै
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.684)
- **Original**: 36 दक्षो मरीचिरक्रिश्व भृष्वाह्याश्न प्रजेश्वरा:। जगत्यत्र महाभाग नित्यसर्गस्थ हेतव:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.685)
- **Original**: 37 मनबो मनुपुत्राक्ष भूपा वीर्यधराश्च ये। सम्मार्गनिरता: शूरास्ते सर्वे स्थितिकारिण:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.686)
- **Original**: 38 श्रीमैत्रेय उवाच येय॑ नित्या स्थितिर्ग्रह्मप्नित्यसर्गस्तथेरितः । नित्याभावश् तेषां वै स्वरूपं मर कथ्यताम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.687)
- **Original**: । 39 अपराशर उवाच सर्गस्थितिविनाझांक्ष भगवान्मधुसूदन: । सैस्तै रूपैरचिन्त्यात्मा करोत्यव्याहतो विभुः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.688)
- **Original**: 40 नैमित्तिकः प्राकृतिकस्तथैवात्यन्तिको द्विज । नित्यश्न सर्वभूतानां प्रलयो5यं चतुर्विध:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.689)
- **Original**: 49 प्रथम अंदा 25 पुलह, क्रतु, अञ्रि, यसि_--इन मुनिर्यों तथा अग्रि और पितरोंने अहण किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.690)
- **Original**: श्रद्धासे काम, चला (लक्ष्मी) से दर्प, पूत्तिसे नियम, तुश्टिसे सत्तोष और पृष्टिसे स्तरेभकी उत्पत्ति हुई
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.691)
- **Original**: तथा मेधासे श्रुत, क्रियासे दण्ड, नय और विनय, खुद्धिसे ओध, लज्जासे विनय, ठपुसे उसका पुत्र व्यवसाय, शात्तिसे क्षेप, सिद्धिसे सुक्ष और कीर्तिसे यहाका जन्प हुआ; ये ही धर्मके पुत्र हैं। रतिने कामसे धर्मके पौत्र हर्षको उत्पन्न किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.692)
- **Original**: 29--31 # अधर्मकी स्त्रो हिसा थी, उससे अनुव नामक पुत्र और निकृति वामकी कन्या उत्पन्न हुई। उन दोनोंसे भय नासकी कन्याएँ, हुईं । उनमेंसे मायाने समस्त प्राणियोंका संहारकर्ता मृत्यु नामक पुत्र उत्पन्न किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.693)
- **Original**: बेदनाने भो रौस्व (नरक) के द्वारा अपने पुत्र दुःखको जन्म दिया और मृत्युसे व्याधि, जरा, ग्रोक, तृष्णा और क्रोधकी उत्पत्ति हुई
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.694)
- **Original**: ये सब अधर्मरूप हैं ओर 'दुःखोत्तर' नामसे प्रसिद्ध हैं, [क्योंकि इनसे परिणाममें दुःख ही प्राप्त होता है] इनके न कोई स्त्री है और न सनन्‍्तान
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.695)
- **Original**: ये सच ऊर्ध्वश्ता हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.696)
- **Original**: हे मुनिकुमार ! ये भगवान्‌ विष्णुके बड़े भयदुर रूप हैं और ये ही संसारके नित्य-पलयके कारण होते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.697)
- **Original**: है महाभाग ! दक्ष, मरीधि, आत्रि और भृयु आदि प्रजापतिंगण इस जगतके नित्य-सर्गक्के कारण हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.698)
- **Original**: 37। तथा मनु और मनुके पराक्रमों, सम्माएपरायण और शुर-वीर पुत्र रुजागण इस सँसारकी नित्य-स्थितिके कारण हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.699)
- **Original**: श्रीमैत्रेयजी खोले--हे ब्रह्मन्‌ ! आपसे जो नित्य- स्थिति, नित्य-सर्ग और नित्य-प्रकयका उल्लेख किया सो कुपा करके मुझसे इनक्य्र स्वरूप वर्णन कीजिये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.700)
- **Original**: श्रीपराज्जजी बोले--जिनकां गति कहीं नहीं रुकती जे अचित्त्यात्मा सर्वव्यापक भगवान्‌ मपैसूदन निरन्तर इन मनु आदि कृूपोंसे संसारकी उत्पत्ति, स्थिति और ना करते रहते हैं
- **Translation**: 

---

