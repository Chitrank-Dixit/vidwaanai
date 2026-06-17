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

### Verse 1 (Vishnu Puran 0.2261)
- **Original**: 70 मां जानीत बयं बाला देही देहेषु शाश्वत: । जरायोबनजन्माद्या धर्मा देहस्य नात्मगः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2262)
- **Original**: 79 बाल्ओेउहे तावदिच्छातो यतिष्ये श्रेयसे युवा । युवाहं वार्डके प्राप्ते करिष्याम्यात्मनो हितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2263)
- **Original**: 72 वृद्धे5हं मस्त कार्याणि समस्तानि न गोचरे । कि करिष्यामि मन्दात्मा समर्थेन न बत्कृतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2264)
- **Original**: 73 एवं दुराशया क्षिप्तमानस: पुरुष: सदा। श्रेयसोउभिमुखं याति न कदाचित्पिपासित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2265)
- **Original**: 74 बाल्ये क्रीडनकासक्ता यौवने विषयोन्मुखा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2266)
- **Original**: अज्ञा नयन्यझकत्या च वार्डक समुपस्थितम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2267)
- **Original**: 75 तस्माद्वाल्ये विवेकात्मा यतेत श्रेयसे सदा । बाल्ययोवनव॒द्धाददेहभावरसंयुत: ..._
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2268)
- **Original**: 76 तदेतद्वो मयाख्यातं यदि जानीत नानृतम्‌। तदस्मत्परीतये विष्णु: स्पर्यतां बन्धमुक्तिदः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2269)
- **Original**: 77 प्रयास: स्मरणे को5स्य स्पृतो यच्छति झोभनम्‌ । पापक्षयश्च॒भवति स्मरता तमहनिशय्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2270)
- **Original**: 78 सर्वभूतस्थिते तस्मिन्मतिमैंत्री दिबानिशम। भवतां जायतामेब॑ सर्वक्षेशायप्रह्स्यथ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2271)
- **Original**: 79 तापत्रयेणाभिहत॑ बदेतदखिलें. जगत्‌। तदा शोच्चेषु भूतेषु हवेष प्राज़: करोति कः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2272)
- **Original**: 80 अथ भरद्राणि भूतानि हीनहक्तिरह॑ परम्‌। मु्दं तदापि कुर्बीत हानिद्ेपफल यतः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2273)
- **Original**: 891 आदिकी भावनासे पदार्थ-नाशका दुःख प्राप्त हो जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2274)
- **Original**: इस प्रकार जीते-जी तो यहाँ महान्‌ दुःख होता ही है, मरनेपर भी यम-यातनाओंका और गर्भ- प्रवेशका ठग्य कष्ट भोगना पड़ता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2275)
- **Original**: यदि तुम्हें गर्भवासमें लेझमात्र भी सुखका अनुमान होता हो तो कड़ों। सारा संसार इसी प्रकार अत्यन्त दुःखमय है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2276)
- **Original**: इसल्ल्ये दुःस्वॉके परम आश्रय इस संसार- समुद्रमें एकमात्र विष्णुभगवान्‌ ही आप स्मेगॉकी परमगति हैं--यह मैं सर्वधा सत्य कहता हूँ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2277)
- **Original**: ऐसा मत समझो कि हम तो अभी बालक हैं, क्‍योंकि जरा, यौबन और जन्म आदि अवस्थाएँ तो देहके ही धर्म हैं, शरीरका अधिष्ठाता आत्मा तो नित्य है, उसमें यह कोई धर्म नहीं है । 71
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2278)
- **Original**: जो मनुष्य ऐसी दुराज्ाओंसे विक्षिप्तचित्त रहता है कि 'अभी मैं बालक हूँ इसलिये इच्छानुसार स्वेल-कूद लूँ, युवावस्था प्राप्त होनेपर कल्याण-साधनका यज्र करूँगा ।' [ फिर युवा होनेपर कहता है कि ] “अभी तो मैं युवा हूँ, बुढ़ापेमें आत्मकल्याण कर लुँगा।' और [ वृद्ध होनेपर सोचता है कि ] “अब मैं बूढ़ा हो गया, अब तो मेरी इन्द्रियाँ अपने कर्मोँमें प्वृत्त ही नहीं होतीं, इरीस्के विधिलः हो जानेपर अब मैं क्या कर सकता हूँ 2? सापर्ध्य रहते तो मैंने कुछ किया हो नहीं ।' वह अपने कल्याण- पथपर कभी अग्रसर नहीं होता; केबल भोग-तृष्णामें ही व्याकुछ रहता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2279)
- **Original**: 72--74
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2280)
- **Original**: मूर्खछोग अपनी बाल्यावरधार्में खेल कूदमें लगे रहते हैं, युवावस्थामें विषयोंमें फैंस जाते हैं और बुढ़ापा आनेपर उसे असमर्थताके कारण व्यर्थ ही काटते हैं
- **Translation**: 

---

