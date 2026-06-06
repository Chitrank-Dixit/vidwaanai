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

### Verse 1 (Rig Ved 0.421)
- **Original**: 188. ये महो रजसो विदुर्विश्वे देवासो अहुह:। मरुद्धिरग्न आ गहि
- **Translation**: 

---

### Verse 2 (Rig Ved 0.422)
- **Original**: जो मरुद्‌गण पृथ्वी पर श्रेष्ठ जल वृष्टि करने की (विधि जानते हैं या) क्षपता से सम्पन हैं। हे अभ्निदेव ! आप उन द्रोहरहित मरुदूगणों के साथ इस बज्ञ में पधारें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.423)
- **Original**: 189. य उ्ना अर्कमानृचुरनाधृष्टास ओजसा। मरुद्धिरर्न आ गहि
- **Translation**: 

---

### Verse 4 (Rig Ved 0.424)
- **Original**: हे अग्निदेव ! जो अति बलशाली, अजेय और अत्यन्त प्रचण्ड सूर्य के सदृश प्रकाशक हैं। आप उन मरुदगणों के साथ यहाँ पधारें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.425)
- **Original**: 190. ये शुभ्रा घोरवर्पस: सुक्षत्रासो रिशादस:। मरुद्धिरग्न आ गहि
- **Translation**: 

---

### Verse 6 (Rig Ved 0.426)
- **Original**: जो शुध्र तेजों से युक्त, तीक्ष्ण, वेधक रूप वाले, श्रेष्ठ बल - सम्पनन और शत्रु का संहार करने वाले हैं। है अग्निदेव ! आप उन मतों के साथ यहाँ पधारें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.427)
- **Original**: श्र ऋः़्वेद संहिता भाग-9 191. ये नाकस्याधि रोचने दिवि देवास आसते। मरुद्धिररन आ गहि
- **Translation**: 

---

### Verse 8 (Rig Ved 0.428)
- **Original**: हे अग्निदेव ! ये जो मरदूगण सबके ऊपर अधिष्ठित, प्रकाशक घुलोक के निवासी हैं, आप उन मरुद्‌गणों के साथ पथारें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.429)
- **Original**: 192. य ईड्डुयन्ति पर्वतान्‌ तिरः समुद्रमर्णवम्‌। मरुद्धिरग्न आ गहि
- **Translation**: 

---

### Verse 10 (Rig Ved 0.430)
- **Original**: है अग्निदेव ! जो पर्वत सदृश विशाल प्रेघों को एक स्थान से सुदूरस्थ दूसरे स्थान पर ले जाते हैं तथा जो शान्त समुद्रों में भी ज्वार पैदा कर देते हैं (हलचल पैदा कर देते हैं), ऐसे उन मरुदगणों के साथ आप यज्ञ में पथारें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.431)
- **Original**: 193. आ ये तन्वन्ति रश्मिभिस्तिर: समुद्रमोजसा । मरुद्धिरग्न आ गहि
- **Translation**: 

---

### Verse 12 (Rig Ved 0.432)
- **Original**: है अग्निदेव ! जो सूर्य की रश्मियों के साथ संव्याप्त होकर समुद्र को अपने ओज से प्रभावित करते हैं , उन मरुतों के साथ आप यहाँ पधारें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.433)
- **Original**: 194. अभि ला पूर्वपीतये सृजामि सोरम्य मधु। मरुद्धररन आ गहि
- **Translation**: 

---

### Verse 14 (Rig Ved 0.434)
- **Original**: है अग्निदेव ! सर्वप्रथम आपके सेवनार्थ यह मधुर सोमरस हम अर्पित करते हैं, अत: आप मसर्तों के साथ यहाँ पथारें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.435)
- **Original**: [ सूक्त - 20 ] [ऋषि- मेधातिथि काण्व । देवता-ऋभुगण । छन्द-गायत्री
- **Translation**: 

---

### Verse 16 (Rig Ved 0.436)
- **Original**: ] 195, अयं देवाय जन्मने स्तोमो विप्रेभिरासया। अकारि रल्लधातम:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.437)
- **Original**: ऋभुदेवों के निमित्त ज्ञानियों ने अपने मुख से इन रमणीय स्तोत्रों की रचना की तथा उनका पाठ किया
- **Translation**: 

---

### Verse 18 (Rig Ved 0.438)
- **Original**: 196. य इन्द्राय बचोयुजा ततक्षुर्ममसा हरी । शमीभिर्यज्ञ़माशत
- **Translation**: 

---

### Verse 19 (Rig Ved 0.439)
- **Original**: जिन ऋषुदेवों ने अतिकुशलतापूर्वक इन्द्रदेव के लिए वचन मात्र से नियोजित होकर चलने वाले अश्वों की रचना की, ये शमी आदि (यज्ञ पात्र अथवा पाप शमन करने याले देवों ) के साथ यज्ञ में सुशोभित होते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.440)
- **Original**: [चिप एक प्रकार के पात्र का नाम है, जिसे भी देव भाव से समजोधित किया गया है ।
- **Translation**: 

---

