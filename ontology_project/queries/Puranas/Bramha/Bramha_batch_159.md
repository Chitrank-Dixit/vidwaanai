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

### Verse 1 (Bramha 0.3161)
- **Original**: आप सर्वथा दुःख छोड़कर शान्ति धारण कीजिये इसमें मुझे व्याधका अपराध नहीं जान पड़ता। तुम
- **Translation**: 

---

### Verse 2 (Bramha 0.3162)
- **Original**: और अपनी बुद्धिको शुभमें लगाकर धर्मका सम्पादन अपनी धर्ममयी बुद्धिको दृढ़ करो। ब्राह्मणोंके गुरु
- **Translation**: 

---

### Verse 3 (Bramha 0.3163)
- **Original**: कीजिये। दूसरोंके द्वार किये हुए उपकार और अग्रि हैं। सब वर्णोंका गुरु ब्राह्मण है। स्त्रियॉँका गुरु
- **Translation**: 

---

### Verse 4 (Bramha 0.3164)
- **Original**: अपकार दोनों ही साधु पुरुषोंके विचारसे श्रेष्ठ हैं। उसका पति है और सब लोगोंका गुरु अभ्यागत है।
- **Translation**: 

---

### Verse 5 (Bramha 0.3165)
- **Original**: उपकार करनेवालॉपर तो सभी उपकार करते हैं। जो लोग अपने घरपर आये हुए अतिथिको वचनोंद्राय
- **Translation**: 

---

### Verse 6 (Bramha 0.3166)
- **Original**: अपकार करनेवालोंके साथ जो अच्छा बर्ताव करे, संतुष्ट करते हैं, उनके उन वचनोंसे वाणीकी
- **Translation**: 

---

### Verse 7 (Bramha 0.3167)
- **Original**: वही पुण्यका भागी बताया गया है प॑: + तुष्टे भर्तरि नारौणां तुष्टा: स्युः सर्वदेवता:। विपर्ययें तु॒नारीणामवश्यं॑ नाशमाधुयात्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.3168)
- **Original**: त्वं दैव॑ त्व॑ प्रभुर्माहं त्व॑ं सुद्ृत्व॑परायणम्‌
- **Translation**: 

---

### Verse 9 (Bramha 0.3169)
- **Original**: त्ब॑ ब्रतं त्व॑ परं ब्रह्म स्वर्गों मोक्षस्त्वमेव च
- **Translation**: 

---

### Verse 10 (Bramha 0.3170)
- **Original**: 40-44 ) नै गुरुरप्रिट्ठिजातीनां यर्णानां ब्राह्मणों गुरु:
- **Translation**: 

---

### Verse 11 (Bramha 0.3171)
- **Original**: पतिरेव गुरु: स्त्रौणां सर्वस्पाभ्यागतों गुरु:। अध्यागतमनुप्रापं वचतैस्तोषयन्ति._ ये
- **Translation**: 

---

### Verse 12 (Bramha 0.3172)
- **Original**: तेषां ख्ागीश्वरी देवों तृत्ता भवति निश्चितम्‌। तस्यान्नस्थ प्रदानेन शक्रस्तृप्तिमवाप्नुयात्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.3173)
- **Original**: पितर: पादशौचेन अज्नाच्चेन प्रजापति:। तस्योपचाराद्द लक्ष्मीर्विष्णुना प्रौतिमाप्रुयात्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.3174)
- **Original**: शयने सर्वदेवास्तु तस्मात्यूज्यतमोउतिथि:
- **Translation**: 

---

### Verse 15 (Bramha 0.3175)
- **Original**: अभ्यागतमनुश्नान्त॑ सूर्योद॑ गृहमागतम्‌
- **Translation**: 

---

### Verse 16 (Bramha 0.3176)
- **Original**: तस्मिन्‌ हि तृप्ते मुदवाप्रुवन्ति गते निशाशेडपि च ते निराशा:
- **Translation**: 

---

### Verse 17 (Bramha 0.3177)
- **Original**: 47-52) + उपकारो5पकारक्ष प्रवागाविति सम्मतौ । उपकारिषु सर्वोडपि करोत्युपकृतिं पुनः
- **Translation**: 

---

### Verse 18 (Bramha 0.3178)
- **Original**: अपकारिषु यः साधु: पुण्यभाक्‌ स ठदाइत:
- **Translation**: 

---

### Verse 19 (Bramha 0.3179)
- **Original**: (80। 54-55)
- **Translation**: 

---

### Verse 20 (Bramha 0.3180)
- **Original**: * याराहतीर्थ, कुशावर्त, नीलगड्ा और कपोततीर्थकी महिमा + 153 6222222222..2....2-.22..2...-3:ककक क्र अल '्:)::?ओओओओआश्ख ननससच्च्य्च्पपपरपरिटिपरटटटटसि₹ञच2्कष्््््ः कपोत बोला--सुमुखि! तुमने हम दोनोंके
- **Translation**: 

---

