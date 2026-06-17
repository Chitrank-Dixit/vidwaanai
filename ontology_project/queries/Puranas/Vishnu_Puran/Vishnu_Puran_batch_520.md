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

### Verse 1 (Vishnu Puran 0.10381)
- **Original**: 46 अरिष्टो धेनुकः केशी ल्लीलयैब महात्मना । निहता येन दुर्वेत्ता दृश्यतामेष सोउच्युतः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10382)
- **Original**: 47 अर्य॑ चास्य महाबाहूर्बलभद्रोउप्रतो5प्रज: । प्रयाति छीलया योषिन्मनोनयननन्दन:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10383)
- **Original**: 48 अरय॑ स कथ्यते प्राज़ै: पुराणार्थविशारदै: । गोपाल्छो यादव वंश मग्ममभ्युद्धरिष्यति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10384)
- **Original**: 49 अय॑ हि सर्वकोकस्य विष्णोरखिलजन्मन: । अयतीर्णो महीमंशो नून॑ भारहरों मुबः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10385)
- **Original**: 50 इत्येव॑ वर्णिते पौरे रामे कृष्णे ख तत्क्षणात्‌ । उरस्तताप देवक्या: स्लेहस्लुतपयोधरम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10386)
- **Original**: 59 महोत्सवमिवासाद्य पुत्राननविलोकनात्‌ । युबेब॒बसुदेवो5भूद्विहायाभ्यागतां जराम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10387)
- **Original**: 52 पद्ञम अंधा 3657 बलमें ऐशवतके समान उस महाबली हाथीकी सूँड अपने हाथसे पकड़कर उसे घुमाया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10388)
- **Original**: भगवान्‌ कृष्ण यद्यपि सम्पूर्ण जगतके स्वामी हैं तथापि उन्होंने बहुत देस्तक उस हाथीके दाँत और चरणोंके बीचमें खेलते- खेलते अपने दाएँ हाथसे उसका नायाँ दाँत उखाड़कर उससे महाबतपर प्रहार किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10389)
- **Original**: इससे उसके सिरके सैकड़ों टुकड़े हो गये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10390)
- **Original**: उसी समय वलभद्रजीने भी क्रोधपुर्वक उसका दायाँ दाँत उखाड़कर उससे आस-पास खड़े हुए महावतोंको मार डाल्झा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10391)
- **Original**: तदनन्तर महाबली रोहिणीनन्दनने रोषपूर्वक अति लेगसे उछऊूकर उस हाथीके मस्तकपर अपनी बायीं ल्खत सारी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10392)
- **Original**: इस प्रकार वह हाथी बलभद्रजीडारा लीलापूर्वक मारा जाकर इच्ध-वद्धसे आहत पर्वतके समान गिर पड़ा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10393)
- **Original**: तब महाबतसे प्रेरित कुबलयापीडकों मारकर उसके मद और रक्तसे लूथ-पथ राम और कृष्ण उसके दांतोंको लिये हुए गर्वयुक्त लील््रमयो चितवनसे निहारते उस महान्‌ रेगभूमियें इस प्रकार आये जैसे मृग-समूहके जीचमें सिंह चल्म जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10394)
- **Original**: उस समय महान्‌ रैगभूमिमें बड़ा फोलछाहल होने लगा और सब ल्म्रेगोमें “ये कृष्ण हैं, ये बलभद्र हैं' ऐसा विस्मय छा गया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10395)
- **Original**: [वे कहने र्ूगे--- ] “जिसने बालघातिनी घोर राक्षसी पूतनाको मारा था, शकटकों उलट दिया था और यमलार्जुनको उस्ताड़ डाला था वह यहीं है। जिस बालकने कालियनागके ऊपर चढ़कर ठसक्व मान-मर्दन किया था और सात रात्रितक महापर्वत गोवर्धनको अपने हाथपर घारण किया था यह यही है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10396)
- **Original**: जिस महात्माने अरिश्टसुर, घेनुकासुर और केझ्ी आदि दुष्टोंको ल्लीछासे ही मार डाल्छा था; देखो, वह अच्युत यही हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10397)
- **Original**: ये इनके आगे इनके बड़े भाई महाबाहुबल- भद्रजी हैं जो बड़े स्लीलापूर्वक चल रहे हैं। ये स्नियोंके मन और नयनॉंको बड़ा ही आनन्द देनेवाले हैं 7
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10398)
- **Original**: पुराणार्थवेत्ा विद्वान्‌ स्त्रेग कहते हैं कि ये पालजी ने हुए यदुवंशका उद्धार करेंगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10399)
- **Original**: ये सर्वल्लेकमय सर्वकारण भगबान्‌ बिष्णुक्रे ही अंडा हैं, इन्होंने पृथिजीका भार उतारनेके लिये ही भूमिपर अवतार लिया है”
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10400)
- **Original**: राम और कृष्णके विषयमें पुरखासियोकि इस प्रकार कहते समय देखकोके स्तनोंसे स्न्रेहके कारण दूध बहने लगा और उसके द्वदयमें बड़ा अनुताप हुआ
- **Translation**: 

---

