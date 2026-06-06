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

### Verse 1 (Sama Ved 0.341)
- **Original**: अदिति 1021 छन्द - गायत्री 1-34
- **Translation**: 

---

### Verse 2 (Sama Ved 0.342)
- **Original**: बृहती-35-62
- **Translation**: 

---

### Verse 3 (Sama Ved 0.343)
- **Original**: व्रिप्टप्‌ 63, 65, 67-71, 73-80 । जगती 64, 66 अनुष्टुप्‌ 81-96 । उष्णिक्‌ 97-1 14
- **Translation**: 

---

### Verse 4 (Sama Ved 0.344)
- **Original**: इति आग्नेयपर्वणि प्रथमो5 ध्याय: ।
- **Translation**: 

---

### Verse 5 (Sama Ved 0.345)
- **Original**: । जा 07 400 जय #एण
- **Translation**: 

---

### Verse 6 (Sama Ved 0.346)
- **Original**: ऐन्द्रं पर्व
- **Translation**: 

---

### Verse 7 (Sama Ved 0.347)
- **Original**: अथ द्वितीयो5 ध्याय:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.348)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.349)
- **Original**: 115. तद्ठो गाय सुते सचा पुरुहूताय सत्वने । श॑ यद्गवे न शाकिने
- **Translation**: 

---

### Verse 10 (Sama Ved 0.350)
- **Original**: हे स्तोताओ ! सोमरस तैयार हो जाने के पश्चात्‌ अनेक लोग जिनकी स्तुति करते हैं, उन बलवान्‌ इन्धदेव के लिए, एक साथ सब मिलकर स्तुति करें । इससे इद्धदेव को बैसा ही सुख प्राप्त होगा, जैसे गाय को घास से मिलता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.351)
- **Original**: 116. यस्ते नूनं शतक्रतविन्द्र द्युम्नितमो मदः
- **Translation**: 

---

### Verse 12 (Sama Ved 0.352)
- **Original**: तेन नूनं मदे मदेः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.353)
- **Original**: है शतकर्मा इद्धदेव ! आपके लिए अत्यन्त तेजस्वी, अभिषुत किया हुआ सोमरस तैयार हैं। उसको पान करके आप तृप्त हों और धनादि देकर हमको आनन्दित करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.354)
- **Original**: 117. गाव उप वदावटे मही यज्ञस्य रप्सुदा । उभा कर्णा हिरण्यया
- **Translation**: 

---

### Verse 15 (Sama Ved 0.355)
- **Original**: सूर्य रश्मियाँ यज्ञार्थ स्थित, उस पृथ्वी को (अन्नादि उत्पन्न करके) यज्ञीय रूप प्रदान करने वाली हैं, जिसके दोनों छोर चमकीले हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.356)
- **Original**: [प्र्वी के दोनों ध्ुवों पर चुम्बकीय तरंणों का प्रचण्ड प्रवाह है, चुम्बक्लीय ऊर्जा के कारण उन्हें चमकीला कहा गया है ।] 118. अरमश्वाय गायत श्रुतकक्षारं गवे । अरमिद्धस्य धाम्ने
- **Translation**: 

---

### Verse 17 (Sama Ved 0.357)
- **Original**: हे श्रुतकक्ष-त्र्रष
- **Translation**: 

---

### Verse 18 (Sama Ved 0.358)
- **Original**: आप गौओं, अश्वों और इन्द्रदेब के आवास (स्वर्ग) की प्राप्ति के लिए पर्याप्त स्तोत्रों का गान करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.359)
- **Original**: 119. तमिद्धं वाजयामसि महे वृत्राय हन्तवे । स वृषा वृषभो भुवत्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.360)
- **Original**: जो बृत्रहन्ता हैं, हम स्तोता उनकी प्रशंसा और स्तुति करते हैं, वे दाता इन्द्र हमें धन-धान्य से पूर्ण करें
- **Translation**: 

---

