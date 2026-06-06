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

### Verse 1 (Vishnu Puran 0.12021)
- **Original**: 23 अनावृष्टिभयप्राया: प्रजा: क्षुद्धधकातरा: । भविष्यन्ति तदा सर्वे गगनासक्तदृष्टय:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12022)
- **Original**: 24 कन्दमूछफलाहारास्तापसा इव मानवा: । आत्मानं घातयिष्यन्ति ह्ानावृष्टयाद्दि:खिता:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12023)
- **Original**: 25 वर्णोंसे कन्या अहण करनेमें समर्थ होगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12024)
- **Original**: उस समय द्विजातिगण जिस-किसी उपायसे [ अर्थात्‌ निषिद्ध द्रव्य आदिसे ] भी 'दीक्षित' हो जायैंगे और जैसी-तैसी क्रियाएँ ही प्रायश्चषित मान ली जायैंगी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12025)
- **Original**: हे द्विज ! कलियुगमें जिसके मुखसे जो कुछ निकल जायगा यही शास्त्र समझा जायगा; उस समय सभी (घूत- ग्रेत-मज्ञान आदि) देवता होंगे और सभीके सब आश्रम होंगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12026)
- **Original**: उपलास, तीर्थाटनादि कायफ्रेश, धन-दान तथा तप आदि अपनी रुचिके अनुसार अनुष्ठान किये हुए ही धर्म समझे जायैंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12027)
- **Original**: कलियुगमें अल्प धनसे ही ल्मेगोंको घनाह्यताका गर्व हो जायगा और केशोंसे ही ख्रियोंको सुन्दरताका अभिमान होगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12028)
- **Original**: उस समय सुवर्ण, मणि, रत्न और वस्त्रोंके क्षीण हो जानेसे स्त्रियाँ केझ-कल्म्रपॉसे ही अपनेको विभूषित करेंगी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12029)
- **Original**: जो पति धनहीन होगा उसे स्त्रियाँ छोड़ देंगी। कलियुगमें घनवान्‌ पुरुष ही स्त्रियॉकत्र पति होगा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12030)
- **Original**: जो मनुष्य [ चाहे वह कितनाहू निन्‍्छ्य हो ] अधिक धन देगा वहीं स्त्रेगॉंका स्वामी होगा; यह धन- दानका सम्बन्ध ही स्वामित्वका कारण होगा, कुलीनता नहों
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12031)
- **Original**: कलियमें सारा द्रष्य-संग्रह घर अनानेमें ही समाप्त हो जायगा [ दान-पुण्यादिमें नहीं ], बुद्धि धन-सख्जरयमें ही लगी रहेगी [ आल्ज्ञानमें नहीं ], सारी सम्पत्ति अपने उपभोगमें ही नष्ट हो जायगी [ उससे अतिथिसत्कारादि न होगा ]
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12032)
- **Original**: कलिकालमें स्त्रियाँ सुन्दर पुरुषकी कामनासे स्वेच्छाचारिणी होंगी तथा पुरुष अन्यायेपार्जित धनके इच्छुक होंगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12033)
- **Original**: हे द्विज ! कलियुगमें अपने सुद्ददोंके प्रार्था करनेपर भी ल्लेग एक-एक दमड़ीके लिये भी स्वार्थहानि नहीं करेंगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12034)
- **Original**: कलियमें ब्राह्मणोंके साथ झूद्र आदि समानताका दावा करेंगे और दूध देनेके कारण ही गौओंका सम्मान होगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12035)
- **Original**: उस समय स्पूर्ण प्रजा क्षुधाकी व्यथासे व्याकुल हो प्रायः अनावृष्टिके भयसे सदा आक्य्रशाकी ओर दृष्टि लगाये रहेगी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12036)
- **Original**: मनुष्य [ अन्नका अभाव होनेसे ] तपस्वियोंके समान केवल कन्द, मूल और फल आदिके सहारे ही रहेंगे तथा अनावृष्टिके कारण दु:ख्री होकर
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12037)
- **Original**: आअन्1] दुर्भिक्षेव सतते तथा क्लेशमनीश्चराः । प्राप्ययन्ति व्याहतसुखप्रमोदा मानबाः कलौ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12038)
- **Original**: 26 अस्त्रानभोजिनो नाभख्रिदेवतातिथिपूजनम्‌ । करिष्यन्ति कलौ प्राप्ते न चर पिण्डोदकक्रियाम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12039)
- **Original**: 27 लोलुपा . हस्वदेहाश॒ बहुन्नादनतत्परा:। बहुप्रजाल्पभाग्याश्न भविष्यन्ति कल ख्रिय:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12040)
- **Original**: 28 उभ्नाभ्यामपि पाणिभ्यां शिरः:कण्डूबन ख्लियः। कुर्वन्यो गुरुभर्तृणामाज्ञां भेत्यन्यनादरा:
- **Translation**: 

---

