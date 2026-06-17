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

### Verse 1 (Vishnu Puran 0.9481)
- **Original**: गोपोने कहा--भैथा राम और कृष्ण! इस भूमिप्रदेशकी रक्षा सदा घेनुकासुर करता है, इसीलिये यहाँ ऐसे पके-प्के फल लगे हुए हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9482)
- **Original**: अपनी गख्से सम्पूर्ण दिद्ञाऑकी आमोदित करनेबाले ये ताल-फल तो देखो; हमें इन्हें खानेक्ो इच्छा है; यदि आपको अच्छा लगे तो [ थोड़े-से ] झाड़ दीजिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9483)
- **Original**: श्रीपराशरजी बोले--गोपकुमारोकि ये वचन सुनकर बलरामजीने ऐसा ही करना चाहिये यह कहकर फल गिर दिये और पीछे कुछ फल कणचच्धते भी पृथिवीपर गिराये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9484)
- **Original**: गिरते हुए फलोॉंका शब्द सुनकर बह दुर्द्धव और दुरात्मा गर्दभासुर क्रोधपूर्वक दौड़ आया और उस महाबलवान्‌ असुरने अपने पिछले दो पैरोंसे बलरामजोको झातोमें लात मारी । बल्रामजीने उसके ठन पैरोंकों पकड़ लिया और आकाझशमें घुमाने लगे। जब वह निर्जीव हो गया तो उसे अत्यन्त बेगसे उस ताल-वक्षपर ही दे मारा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9485)
- **Original**: उस गधेने गिरते-गिरते उस तालबुध्षसे बहुत-से फल्ड इस प्रकार गिस दिये जैसे प्रचण्ड बायु बादलॉको गिरा दे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9486)
- **Original**: उसके सजातीय अन्य गर्दभासुरोंक आनेपर भी कृष्ण और यामने उन्हें अनायास ही ताल-वृक्षॉपर पटक दिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9487)
- **Original**: हे मैत्रेय ! इस प्रकार एक क्षणमें ही पके हुए तालफल्में और गर्दभासुरोंके देहोंसे विभूषिता होकर पूृथिवी अत्यन्त सुशोभित होने छगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9488)
- **Original**: हे द्विज ! तबसे उस ताल्वनमें गौएँ निर्तिप्त होकर सुखपूर्वक नवीन तृण चरने लगीं जो उन्हें पहले कभी चरनेको नसीब नहीं हुआ था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9489)
- **Original**: इति श्रीविष्णुपुराणे पश्चममेंडशे अष्टरमोइघ्याय:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9490)
- **Original**: जनक शऑै पपयय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9491)
- **Original**: ज्ेकेरे श्रीविष्णुपुराण [ अ0 9 नवाँ अध्याय घ्रलूम्ब-सध श्रीपराज्षर उवाच तस्मित्रासभदैतेये. सानुगे विनिपातिते। सौम्य॑ तज़ोपगोपीनां रम्यं तालबनं बभो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9492)
- **Original**: 9 ततस्तो जातहर्षा तु वसुदेवसुताबुभो । हत्वा थेनुकदैतेय॑ भाण्डीरबटमागतौ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9493)
- **Original**: 2 क्ष्वेलमानौ प्रगायन्तौ विचिन्वन्तौ च पादपान्‌ । चारयन्तो च गा दूरे व्याहरन्तौ च नामभि:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9494)
- **Original**: 3 नियोंगपाशस्क-धौ तो बनमालाविभूषितो । झुशुभाते महात्मानौं बाल्शूज्विवर्षभौ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9495)
- **Original**: 4 सुवर्णाज्ननचूर्णाभ्यां तौ तदा रूषिताम्बरों । महेद्धायुधसंयुक्तो श्वेतकृष्णाविवाम्बुदौ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9496)
- **Original**: 5 चेरतुलोकसिद्धाभि: क्रीडाभिरितरेतरम्‌ । समस्तलोकनाथानां नाथभूतो भुवं गतौ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9497)
- **Original**: 6 मनुष्यधर्माधिरती सानयन्तो मनुष्यताम्‌। तज्जातिगुणयुक्ताभि: क्रीडाभिश्वेरतुर्बनम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9498)
- **Original**: 7 ततस्त्वान्दोलिकाभिश्च नियुद्धौश्न महावलौ । व्यायाम चक्रतुस्तत्र क्षेपणीबैस्तथाइममि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9499)
- **Original**: 8 तल्लिप्सुरसुरस्तत्र ह्रभयो रममाणयो: । आजगाम प्रलम्ब्ाख्यो गोपवेषतिरोहित:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9500)
- **Original**: 9 सो5बगाहत निरशद्डस्तेषां मध्यममानुषः । मानुष बपुरास्थाय प्रलम्यो दानवोत्तमः
- **Translation**: 

---

