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

### Verse 1 (Vishnu Puran 0.2801)
- **Original**: रजः और सत्त्वादि गुणोंके आअ्रयसे थे सनातन प्रभु ही जगतकी रचनाके समय रचना करते हैं, स्थितिके समय पालन करते हैं और अन्तसमयमें कालरूपसे संहार करते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2802)
- **Original**: वे जनार्दन चार विभागसे सृष्टिके और चार विभागसे ही स्थितिके समय रहते हैं तथा चार रूप घारण कस्के ही अन्तमें प्रलय करते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2803)
- **Original**: एक अंझसे वे अव्यक्तस्वरूप ब्रह्मा होते हैं, दूसरे अंशसे मरीचि आदि प्रजापति होते हैं, उनका तोसरा अंश काल है और चौथा सम्पूर्ण प्राणी । इस प्रकार वे स्णोगुणविशिष्ट होकर चार प्रकारसे सृष्टिके समय स्थित होते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2804)
- **Original**: फिर वे पुरुषोत्तम सत्वगुणका आश्रय लेकर जगत्‌की स्थिति करते हैं। उस समय ले एक अश्लसे विष्णु होकर पालन करते हैं, दूसरे अंज्लसे मनु आदि छोते हैं तथा तीसरे अंशसे काल और चौथेसे सर्वभूतोंमें स्थित होते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2805)
- **Original**: तथा अन्तकालमें बे अजन्मा भगवान्‌ तमोगुणकी वृत्तिका आश्रय ले एक अंझसे रुद्ररूप, दूसरे भागसे अप्रि और अन्तकादि रूप, तीसरेसे कालरूप और चौथेसे राम्पूर्ण भूतस्वरूप हो जाते एं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2806)
- **Original**: हे ब्रह्मन्‌ ! बिनाहा करनेके लिये उन महात्माकों यह चार प्रक्कारकी सार्वकालिक विभागकल्पना कही जाती है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2807)
- **Original**: ब्रह्मा, दक्ष आदि प्रजार्पतिगण, काल तथा समस्त प्राणी--ये श्रीहरिक्ी विभूतियाँ जगत्‌की सृष्टिकी कारण हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2808)
- **Original**: आ0 22 ] बिष्णुर्मन्वादय: काल: सर्वभूतानि चर द्विज । स्थितेनिमित्तभूतस्य विष्णोरेता विभूतय:ः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2809)
- **Original**: 32 रद्र: कालान्तकाद्याश्र समस्ताश्चैज जन्तव: । चझतुर्था प्रलयायता जनार्दनविभूतयः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2810)
- **Original**: 33 जगदादौ तथा मध्ये सृष्टिराप्रकया द्विज
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2811)
- **Original**: धात्रा मरीजिमिश्रैश्न क्रियते जन्तुभिस्तथा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2812)
- **Original**: 34 ब्रह्म सृजत्यादिकाले मरीचिप्रमुखास्तत: । उत्पादवन्त्यपत्यानि जन्तवअ प्रतिक्षणम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2813)
- **Original**: 35 कालेन न विना ब्रह्मा सृष्टिनिष्पादको द्विज । न प्रजापतय: सर्वे न चैबवाखिलजन्तव:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2814)
- **Original**: 36 एवमेव विभागो5यं स्थितावप्युपदिश्यते । चतुर्था तस्य देवस्य मैत्रेय प्रलये तथा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2815)
- **Original**: 37 दे गया कक कद थे लत, सत्त्वजातेन लै द्विज । तस्य सज्यस्थ :
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2816)
- **Original**: 38 इन्ति यावज्च यत्किश्नित्सत््व स्थावरजड्रमम्‌ जनार्दनस्थ त्रीद्र मैत्नेयान्तकर॑ बपु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2817)
- **Original**: 39 एबमेष जगल्त्रष्टा जगत्याता तथा जगत्‌। जगद्धक्षयिता देव: समस्तस्थ जनार्दन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2818)
- **Original**: 40 सृष्टिस्थित्यन्तकालेषु त्रिधैल्न॑ सम्प्रवर्तते । गुणप्रवृत््या परम॑ पर्द तस्यथागु्ं महत्‌।
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2819)
- **Original**: 41 तद्च ज्ञानमयं व्यापि स्वसंवेद्यमनोपपमम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2820)
- **Original**: चतुष्प्रकारं तदपि स्वरूप परमात्मनः ।। 42 अ्रोपैत्रेय उताच चतुष्प्रकारतां_तस्य ब्रह्मभूतस्य हे मुने। ममाचक्ष्व यथान्यायं यदुक्त परम पदम्‌
- **Translation**: 

---

