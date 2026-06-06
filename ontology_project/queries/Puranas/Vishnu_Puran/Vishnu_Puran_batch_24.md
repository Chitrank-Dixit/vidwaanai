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

### Verse 1 (Vishnu Puran 0.461)
- **Original**: सबका जप होनेपर भो यह उनके संस्कारोंसे मुक्त नहीं होतो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.462)
- **Original**: हे ब्रह्मन्‌! ब्रह्माजीके सृष्टि-कर्ममें प्रवृत इोनेपर देखताओंसे लेकर स्थावरपर्यन्त चार प्रकारकी सूहि हुई
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.463)
- **Original**: वह केवल मनोमयों थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.464)
- **Original**: फिर देवता, असुर, पितृगण और पनुष्य---इन चार्रोकी तथा जलयाी सृष्टि फरनेको इच्छासे उन्होंने अपने शरीरका उपयोग किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.465)
- **Original**: सृष्टि-रचनाको कामनासे प्रजापतिके युक्तचित होनेपर लमोगुणकी चूद्धि हुईं। अत: सबसे पहले उनको जंकसे असुर उत्सन्न हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.466)
- **Original**: तब, हे मैत्रेय ! उन्होंने उस तमोमय शरैरकों छोड़ दिया, यह छोड़ा हुआ तमोमय झरीर ही रात्रि हुआ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.467)
- **Original**: फिर अन्य देहमें स्थित झ्ोनेफर सृष्टिकी कामनायाले उन प्रज़ापतिको अति प्रसच्रता हुई, और हे द्विज ! उनके मुखसे सत्तप्रधार देखगंण उत्पन्न हुप्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.468)
- **Original**: तदनन्तर उस श्रैस्को भौं उन्होंने ज्थाग दिया। यह त्यापा हुआ शरीर ही सच्लस्वरूप दिल हुआ। इसौलिये गािमें असुर बलयान्‌ होते है और दिल्‍्में देवगणोंका बल विशेष होता, है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.469)
- **Original**: फिर उन्होंने आंशिक सत्वमय अन्य दरीर अह्ण किया और अपनेकों पितृबत्‌ मानते हुए (अपने पार्ख-भागसे] पिठृगणकी रचना की
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.470)
- **Original**: पितृगणक्ररी रचना कर उन्होंने उस वारीरकों थी छोड़ दिया। यह स्यागा हुआ शरीर ही दिन और रात्रिके बीचमें स्थित सख्या हुईं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.471)
- **Original**: तत्पक्षात्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.472)
- **Original**: 28 आविष्णुपुराण ।अ" 5 तामप्याशु स तत्याज तनुं सद्य: प्रजापति: । ज्योत्य्रा समभवत्सापि प्राक्सन्ध्या याउभिधीयते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.473)
- **Original**: 38 ज्योत्सप्तागपे तु बलिनो मनुष्या: पितरस्तथा । पैत्रेय सन्ध्यासमये तस्मादेते भवन्ति खे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.474)
- **Original**: 39 ज्योत्स्रा राग्यहनी सम््या चल्वार्येतानि वै प्रभो: । ब्रह्मणस्तु शरीराणि त्रिगुणोपाश्रयाणि तु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.475)
- **Original**: 40 रजोमात्रात्मिकामेव ततोउन्यां जगृहे तनुम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.476)
- **Original**: उन्होंने ऑदिक रजोमय अन्य हारीर धारण क्रिया; हे ट्विजश्रेष्ट
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.477)
- **Original**: उससे रजः-प्रधान मनुष्य उत्पन्न हुए
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.478)
- **Original**: फिर झीघ्र ही प्रजापतिने उस शरोरको भी त्याग दिया, वही ज्योत्स्ा हुआ, जिसे पूर्व -सम्ध्या अर्थात्‌ प्रातःकाल कहते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.479)
- **Original**: इसोर्ट्यि, हे मैत्रेस ! प्रातःकाल होनेपर मनुष्य और सायकालके समय पितर बल्प्वान्‌ होते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.480)
- **Original**: इस प्रकार रात्रि, दिन, प्रात:काल और सायं॑क्यल ये चारों प्रभू ग्रह्मजीके ही शरीर हैं और तीनों गुणोंके आश्रय हैं
- **Translation**: 

---

