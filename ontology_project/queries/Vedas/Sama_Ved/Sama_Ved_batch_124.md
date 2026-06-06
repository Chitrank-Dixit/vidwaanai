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

### Verse 1 (Sama Ved 0.2461)
- **Original**: । 946.अर्नि वो वृधन्तमध्वराणां पुरूतमम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2462)
- **Original**: अच्छा नप्जे सहस्वते
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2463)
- **Original**: हे ऋत्विज्‌गणों ! आप सब अक्षय शक्ति के भण्डार, पराक्रम को बढ़ाने वाले, परम श्रेष्ठ, तेजस्वी अभ्निदेव के समीप पहुँचें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2464)
- **Original**: 947.अय॑ यथा न आभुवत्त्वष्टा रूपेव तक्ष्या। अस्य क्रत्वा यशस्वत:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2465)
- **Original**: विश्वकर्मा (बढ़ई) जिस प्रकार लकड़ी को संस्कारित करके उत्तम स्वरूप प्रदान करता है, उसी प्रकार इन अग्निदेव के कर्म से हम यशस्त्री होते हैं एवं श्रेष्ठ स्वरूप प्राप्त करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2466)
- **Original**: 948,अयं विश्वा अभि श्रियोग्निर्देवेषु पत्यते । आ बाजैरुप नो गमत्‌
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2467)
- **Original**: सभी प्रकार के ऐश्वर्यों को प्रदान करने वाले हे अग्निदेव ! आप हमारे पास अन्न एवं घन के साथ पधारें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2468)
- **Original**: उत्तराचिकि पत्वमो5ध्याय: 5.9 949.इमभिन्द्र सुत॑ पिब ज्येष्ठममर्त्य मदम्‌। शुक्रस्य त्वाभ्यक्षरन्धारा ऋतस्य सादने
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2469)
- **Original**: हे इन्द्रदेव ! यज्ञशाला में आनन्दवर्द्धक दिव्य सोमरस की धाराएँ, आपको प्राप्त करने के लिए प्रवाहित हो रही हैं। आप इस तेजस्वी सोमरस का पान करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2470)
- **Original**: 950.न किष्ट्वद्रथीतरो हरी यदिन्द्र यच्छसे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2471)
- **Original**: न किष्टवानु मज्मना न कि: स्वश्व आनशे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2472)
- **Original**: अश्वशक्ति से चालित रथ में बैठने वाले हे इन्द्रदेव ! आपसे अधिक पराक्रमी कोई दूसरा वीर नहीं है । आप जैसा कोई अन्य शक्तिशाली, अश्व पालक, घोड़े का स्वामी नहीं है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2473)
- **Original**: 951.इन्द्राय नूनमर्चतोक्थानि च ब्रवीतन । सुता अमत्सुरिन्दवो ज्येष्ठं नमस्यता सह:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2474)
- **Original**: हे ऋ्र््रत्वजो ! आनन्दवर्द्धक, पवित्र सोमरस*समर्पित करके विभिन्न स्तोत्रों से गुणणान करते हुए सब इन्द्र देव की ही पूजा करो । सामर्थ्यशाली उन इद्धदेव को नमस्कार करो
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2475)
- **Original**: 952.3नद्र जुषस्व प्र वहा याहि शूर हरिह । पिबा सुतस्य मतिर्न मधोश्वकानश्वारुर्मदाय
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2476)
- **Original**: हे अश्वपति शूरवीर इन्द्रदेव ! यज्ञशाला में पधार कर आप हमारे द्वारा समर्पित हविष्यान्न को ग्रहण करें । आनन्दवर्द्धक श्रेष्ठ, मधुर सोमरस का इच्छानुसार पान करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2477)
- **Original**: 953.इन्द्र जठर॑ नव्यं न पृणस्थ॒ मधोर्दिवो न। अस्य सुतस्य स्वा3नोंप त्वा मदा: सुवाचों अस्थु:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2478)
- **Original**: हे इन्द्रदेव ! जिस प्रकार अन्तरिक्ष से ध्वनित दिव्य स्तुतियों को सुनकर, आप अनुपम स्वर्ग के आनन्द से लाभान्वित होते हैं, उसी प्रकार इस मधुर पवित्र सोमरस को पीकर तृप्त हों
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2479)
- **Original**: 954. इन्द्रस्तुराषाण्मित्रो न जघान वृत्रं यतिर्न । बिभेद वल॑ भृगुर्न ससाहे शत्रून्मदे सोमस्य
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2480)
- **Original**: शत्रुओं पर शीघ्र विजय पाने वाले हे इन्द्रदेव ! सूर्य कौ तरह मेघ (बृत्र) को, संयमी बीर की भाँति वल राक्षस को एवं सोमरस की शक्ति से सम्पन्न आप भृगु की तरह हमारे शत्रुओं का विनाश करें
- **Translation**: 

---

