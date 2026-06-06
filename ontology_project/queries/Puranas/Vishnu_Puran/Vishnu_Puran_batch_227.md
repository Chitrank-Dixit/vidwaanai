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

### Verse 1 (Vishnu Puran 0.4521)
- **Original**: ऋषभु जोले--हे ट्विजश्रेष्ठ ! मालूम होता है आप यहाँकी सब बातें जानते है। अतः कहियें इनमें राजा कौन है ? और अन्य पुरुष कौन हैं 2
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4522)
- **Original**: निदाघ बोले--यह जो पर्वतके समान कँँचे पत्त गजराजपर चढ़ा हुआ है वही राजा है, तथा दुसरे लोग परिजन हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4523)
- **Original**: ऋतष बोले-- आपने राजा और गज, दोनों एक साथ ही दिखाये, कितु इन दोनोंके पृथक्‌-पृथक्‌ विशेष चिह्न अथवा छक्षण नहीं बतत्मये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4524)
- **Original**: अतः: है महाभाग ! इन दोनोमें क्या-क्या विशेषताएँ है, यह बतत्ताइये । मैं यह जानना चाहता हूँ कि इनमें कौन राजा है और कौन गज है ?
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4525)
- **Original**: निदाघ बोले--इनमें जो नीचे है कह गज है और डसके ऊपर राजा है । हे द्विज ! इन दोनॉंका बाह्य -वाहक- सम्बन्ध है--इस बातको कौन नहीं जानता ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4526)
- **Original**: ऋतु बोले-- [ ठीक है, किन्तु ] हे बहान्‌ ! मुझे इस प्रकार समझाइये, जिससे गैं यह जान सकूँ क्रि 'नोचे' इस दाब्दका वाच्य क्‍या है? और “ऊपर' किसे कहते हैं। 61
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4527)
- **Original**: ब्राह्मणने कहा--ऋभुकेः ऐसा कहनेपर निदाघने जो पूछा है वही यतल्शता हैं---
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4528)
- **Original**: इस समय यजाकी भाँति मैं तो ऊपर हूँ और गजकों भाँति आप नीचे हैं। हे ऋद्यनू ! आपको समझानेके लिये ही मैंने यह दृष्टान्त दिखलाया है''
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4529)
- **Original**: ऋभु बोले--हे द्विजओेप्ट ! यदि आप राजाके समान हैं और मैं गजके समान हूँ तो यह बताइये कि आप कौन हैं? और मैं कौन हूँ 7
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4530)
- **Original**: अन्ए6 ] रत इत्युक्त: सत्वरं तस्य प्रगृह्य] चरणाबुभो। निदाघस्त्वाह भगवानाचार्यस्त्वमृभुर्धुवषम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4531)
- **Original**: 95 नान्यस्थाइैतसंस्कारसंस्कृत मानर्स तथा। यथाचार्यस्य तेन त्वां मन्ये प्राप्तमहं गुरुम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4532)
- **Original**: 16 गुरुस्लेहादूुभु्नाम निदाघ समुषागत:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4533)
- **Original**: 17 तदेतदुपदिष्ट॑. ते महामते । परमार्थसारभूते स्कोर
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4534)
- **Original**: 18 ब्राह्मण उवाच एवमुक्त्वा ययो विद्वाश्चिदाघं स ऋभुर्गुरु: । निदाघो5प्युपदेशेन. तेनाइैतपरो5भवत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4535)
- **Original**: 19 सर्वभूतान्यभेदेन दवुशे स तदात्मन: । यथा ब्रह्मपरो मुक्तिमबाप परमां द्विज:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4536)
- **Original**: 20 तथा त्वमपि धर्मज्ञ तुल्यात्मरिपुलान्धवः । भव सर्वगत जानन्नात्मानमवनीपते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4537)
- **Original**: 29 प्रनरकषमिराद तर्क स्ममर यथैक॑ नभः । दृष्टिभिरा :. सन्पृथक्पूथक
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4538)
- **Original**: 22 एक: समस्तं यदिहास्ति किल्लि .... क्तदच्युतो नास्ति परे ततोउन्यत्‌। सो5हं सच त्वेस च सर्वभित-....... संस लत कज- दात्मस्वरूप॑ त्यज भेदमोहम
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4539)
- **Original**: 23 श्रीफ्रादर उवाच इतीरितस्तेवन स॒ राजवर्य- स्तत्याज भेद॑ परमार्थदृष्टि: । स॒ च्ापि जातिस्मरणाप्तबोधघ- जन्मन्यपवर्गमाप
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4540)
- **Original**: 24 इति भरतनरेन्द्रसारवृत्तं कथयति यश्च श्रूणोति भक्तियुक्त: । स॒ बिमलमतिरेति नात्ममोहं द्वितीय अंडा 161 ब्राह्मणने कहा--ऋभुके ऐसा कहनेपर निदाघने तुरन्त ही उनके दोनों चरण पकड़ ल्यि और कशा-- (निश्चय ही आप आचार्यचरण महर्षि ऋभु हैं
- **Translation**: 

---

