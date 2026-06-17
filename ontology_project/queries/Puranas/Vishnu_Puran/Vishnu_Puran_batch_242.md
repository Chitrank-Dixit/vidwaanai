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

### Verse 1 (Vishnu Puran 0.4821)
- **Original**: 172 172 >> €॒ृ2अउञ़<़॒॒&506&ैञ॒«ः"फब आ फक्‍ फ ऋआ आसमभ्रोयिष्पपुण _>_##॒[ृऔौऔऑइउऑऔऑझऋा/!।]/ 94 श्रोविष्णुपुराण (आ्ड जगत: प्रलयोत्पत्त्योर्यत्तत्कारणसंज्ञितम्‌ । महतः परम गुझहां तस्मे सुब्रह्मणे नमः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4822)
- **Original**: 24 अगाधापारमक्षय्य॑ जगत्सम्मोहनालवम्‌ । स्वप्रकाशप्रवृत्तिभ्यां. पुरुषार्थप्रयोजनम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4823)
- **Original**: 25 सांख्यज्ञानवतां निष्ठा गतिइशमदमात्मनाम्‌ । यक्तदव्यक्तमपृतं प्रवृत्तिब्रह्य शाश्वतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4824)
- **Original**: 26 प्रधानमात्मयोनिश्च गुहासंस्थ च॒ दाब्दयते । अविभागं तथा शुक्रमक्षयं बहुधात्मकम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4825)
- **Original**: 27 परमनत्रह्मणे तस्मे नित्यमेव नमो नमः । यद्रप॑ बासुदेवस्थ परमात्यपस्वरूपिण:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4826)
- **Original**: 28 एतदब्रह्म त्रिधा भेदमभेदमपि स प्रभु: । सर्वभेदेषभेदोउसों भिद्यते भिन्नवुद्धिभि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4827)
- **Original**: 29 स ऋडद्ूमयस्साममय: सर्वात्मा स यजुर्मय: । ऋग्यजुस्सामसारात्मा स एवात्पा शरीरिणाम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4828)
- **Original**: 30 स॒ भिद्यते वेदपयस्सववेद करोति भेदेर्बहुभिस्सशाखम्‌ शाखाप्रणेता स समस्तशास्वा- ज्ञानस्वरूपो.. भगवानसड्रः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4829)
- **Original**: 31 जो संसारके उत्पत्ति और प्रछषका कारण कहल्म्त्म है तथा महत्तत््व्से भी परम गुदा (सृक्ष्म) है उस ऑकाररूप ब्रायफो नमस्कार है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4830)
- **Original**: जो अगाध, अपार और अक्षय है, संसारकों मोहित करनेवाले तमोगुणका आश्रय है, तथा प्रकाशमय सत््वगुण और प्रयृत्तिरूप रजोगुणके द्वारा पुरुषोंके भोग और पोक्षरूप परमपुरुषार्थका हेतु है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4831)
- **Original**: जो सांख्यज्ञानियोँकी परमनिष्ठा है शम-टमशास्थ्योंका गनलब्ध स्थान है, जो अच्यक्त और अबिनाशी है तथा जो सक्रिय ब्रह्म होकर भी सदा रहनेवाला है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4832)
- **Original**: जो स्वयम्भू , प्रधात और अन्तर्याभी कहराता है तथा जो अविभाग, दीप्रिमान्‌, अक्षय और अनेक रूप है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4833)
- **Original**: और जो परमाह्मस्वरूप भगवान्‌ वासुदेबक्य ही रूप (प्रतीक) है, उस ऑकाररूप परब्रह्मफों सर्वदा खासम्बार नमस्कार है 28
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4834)
- **Original**: यह ऑकाररूप ग्रहा अभिन्न होकर भी [ अकार, उकार और मकारूपसे ] तीन भेदोंबात्य है। यह समस्त भ्रेटॉमे अभिन्नरूपसे स्थित है तथापि भेदबुद्धिसे भिन्न-भिन्न प्रतीत होता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4835)
- **Original**: बह सर्वत्मा ऋडूमय, स्रागप्य और यजुर्मय है तथा ऋयजु:- सामका साररूप वह ऑकार ही सब दारीरधारियाँका आत्मा हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4836)
- **Original**: वह चेदमय हैं, बही ऋग्वेदादिरूपसे भिन्न हो जाता है और वहीं अपने वेदरूपको नाना श्ञास्त्राआमें विभक्त करता है तथा वह असंग भागयान्‌ ही समस्त शाखाओंका रचयिता और उनका ज्ञानस्वरूप है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4837)
- **Original**: इति श्रीविष्णुपुराणे तुतोये>शे तृत्तीयोउध्यायः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4838)
- **Original**: ््नञि++ः है $ आंच चोथा अध्याय ऋच्वेदकी ज्ञास्प्राऑका विस्तार अफ्तार उवाच आयो वेदश्वतुष्पाद: शतसाहस्रसम्मित: । ततो दह्शगुणः कृस्स्त्रों यज्ञोड्यं सर्वकामधुक्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4839)
- **Original**: 9 ततो5ब्र मत्सुतो व्यासो अष्टाविंशतिपे5न्तरे । बेदमेक॑ चतुष्पाद॑ चतुर्धा व्यभजत्मभु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4840)
- **Original**: 2 यथा च तेन वे व्यस्ता वेदव्यासेन धीमता । वेदास्तथा समस्तेस्तैर्व्यस्ता व्यस्तैस्तथा मया
- **Translation**: 

---

