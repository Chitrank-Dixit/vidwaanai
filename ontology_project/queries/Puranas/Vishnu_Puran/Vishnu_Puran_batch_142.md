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

### Verse 1 (Vishnu Puran 0.2821)
- **Original**: 43 श्रीपरागर ठवाच मैत्रेय कारणं प्रोक्त साधने सर्ववस्तुषु। साथ्यं चर वस्त्वभिमतं यत्साधवितुमात्मन:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2822)
- **Original**: 4ड योगिनो पुक्तिकामस्य प्राणायामादिसाधनम्‌ । साध्यं च परम ब्रह्म पुनर्नावर्तते यत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2823)
- **Original**: 45 प्रथम अंडा 101 हे द्विज ! विष्णु, मनु आदि, काल और समस्त भूतगण--ये जगत्‌की स्थितिके कारणरूप भगवान्‌ विष्णुकी विभूतियाँ हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2824)
- **Original**: तथा रुद्र, काल, अन्तकादि और सकल जीव--श्रीजनार्दनको ये चार विभूतिसाँ प्ररकूयकी कारणरूप हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2825)
- **Original**: है द्विज ! जगतके आदि और मध्यमें तथा प्रस्ूय- पर्यन्त भी ब्रह्मा, मरोचि आदि तथा भिन्न-भिन्न जीवोंसे हो सृष्टि हुआ करती है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2826)
- **Original**: सृष्टिके आरम्भमें पहले ब्रह्माजी रचना करते हैं, फिर मरीचि आदि प्रजापतिगण और तदननन्‍्तर समस्त जीव क्षण-क्षणमें सन्‍्तान उत्पन्न करते रहते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2827)
- **Original**: हे द्विज ! कालके बिना ब्रह्मा, प्रजापति एवं अन्य समस्त प्राणी भी सृष्टि-रचना नहीं कर सकते [ अतः भगवान्‌ कालूरूप विष्णु ही सर्वदा सृष्टिके कारण हैं ]
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2828)
- **Original**: हे मैत्रेय ! इसरो प्रकार जगतकी स्थिति और प्रलयमें भी उन देवदेवके चार-चार विभाग बताये जाते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2829)
- **Original**: हे द्विज ! जिस किसी जीवद्वारा जो कुछ भी रचना की जाती है उस उत्पन्न हुए जीवकी उत्पत्तिमें सर्वथा श्रीहरिका शरीर हो कारण है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2830)
- **Original**: हे मैत्रेस ! इसी प्रकार जो कोई स्थावर-ज॑गम भूतोमेंसे किसीक्ा नष्ट करता है, वह नाश करनेवाल्म भी श्रीजनार्दनका अन्तकारक रौद्ररूप हो है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2831)
- **Original**: इस प्रकार वे जनार्टनदेव ही समस्त संसारके रचयिता, पाछनकर्ता और संहारक हैं तथा वे ही स्वयं जगत्‌-रूप भी हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2832)
- **Original**: जगतकी उत्पत्ति, स्थिति और अन्तके समय ये इसी प्रकार तीनों गुणोंकी प्रेरणासे प्रवत्त होते हैं, तथापि उनका परमपद महान्‌ निर्गुण है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2833)
- **Original**: परमात्माका वह स्वरूप ज्ञानमय, व्यापक, स्वसंवेद्य (स्वयै-प्रकाश) और अनुपम है तथा वह भी चार प्रकारका ही है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2834)
- **Original**: श्रीमैत्रेयजी बोले--हे मुने! आपने जो प्रगबान्‌का परम पद कहा, वह चार प्रकार कैसे है ? यह आप मुझसे चिधिपूर्वक कहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2835)
- **Original**: श्रीपराधरजी खोल्के--हे मैत्रेय ! सब वस्तुओंका जो कारण होता है बही उनका साधन भी होता है और जिस अपनों अभिमत वस्तुकी सिद्धि की जाती है वही साध्य कहल्ताती है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2836)
- **Original**: मुक्तिको इच्छालाले योगिजनोंके लिये प्राणायाम आदि साधन है और परअह्म ही साध्य है,
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2837)
- **Original**: 102 अ्ीविष्णुपुराण [ आ0 22 साधनालल्‍म्बन ज्ञान मुक्तये योगिनां हि यत्‌ । स भेद: प्रथमस्तस्य ब्रह्मभूतस्थ लै मुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2838)
- **Original**: 46 युद्भतः द्लेझमुक्त्यर्थ साध्यं यद्रह् योगिनः । तदालम्बनविज्ञान॑द्वितीयोंइशो महामुने
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2839)
- **Original**: 47 उभयोस्त्वविभागेन साध्यसाधनयोरहिं यत्‌। विज्ञानमद्दैतमयतद्धागोउन्‍्यों मयोदितः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2840)
- **Original**: 48 ज्ञानत्रयस्य बै तस्य बिशेषों यो महायुने। तन्निराकरणद्वारा दर्शितात्मस्वरूपवत्‌
- **Translation**: 

---

