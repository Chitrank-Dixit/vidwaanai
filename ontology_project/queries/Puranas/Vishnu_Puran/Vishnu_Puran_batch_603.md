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

### Verse 1 (Vishnu Puran 0.12041)
- **Original**: 29 स्वपोषणपरा: श्षुद्रा देहसंस्कारवर्जिता: । परुषानृतभाषिण्यो भविष्यन्ति कलौ स्त्रिय:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12042)
- **Original**: 30 दुःशीला दुष्टशीलेबु कुर्वन््यस्सतत॑ स्पृहाम्‌ । असदतृत्ता भविष्यन्ति पुरुषेषु कुलाड्ना:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12043)
- **Original**: 31 बेदादानं॑ करिष्यन्ति वटवश्चाकृतक्रता: । गृहस्थाश्न न होष्यन्ति न दास्यन्त्युचितान्यपि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12044)
- **Original**: 32 वानप्रस्था भविष्यन्ति ग्राम्याहारपरिग्रहा: । भिक्षवश्षापि मित्रादिस्नेहसम्बन्धयन्त्रणा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12045)
- **Original**: 33 अरक्षितारों हर्त्तारहशुल्कव्याजेन पार्थिवा: । हारिणो जनवित्तानां सम्प्राप्ते तु कौ युगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12046)
- **Original**: 34 यो योअश्वरथनागाछ्मस्त स राजा भविष्यति। यश्च यश्चाबलस्सर्व॑स्स स भृत्यः कत्मे युगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12047)
- **Original**: 35 बैश्या: कृषिबाणिज्यादि सन्त्यज्य निजकर्म यत्‌ । जुद्रवृत्त्या प्रवर््यन्ति कारुकर्मोपजीबिन:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12048)
- **Original**: 36 श्रैक्षग्रतपरा: शुद्रा: प्रव््॒यालिड्विनो5धमा: । पाषण्डसंश्रयां वृत्तिमाश्रयिष्यन्ति सत्कृता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12049)
- **Original**: 37 दुर्भिक्षकरपीडाभिरतीवोपद्वुता गोधूमाक्नयवाध्नाक्यान्देशान्यास्यन्ति दुःखिता:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12050)
- **Original**: 38 बेदमार्गे प्रलीने च पाषण्डाछ्ओे ततो जने । अधर्मवृद्धयया छोकानामल्पमायुर्भविष्यति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12051)
- **Original**: 39 अश्ाख्रविहित घोर तप्यपानेषु ले तपः । नरेषु नृषदोषेण बालये मृत्युर्भविष्यति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12052)
- **Original**: 40 घष्ठ अंश अ्1] ःःःः ःःःःछ अंश ःःसःसःसस स ससःःसछःछः 4257 आत्मघात करेंगे। 25
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12053)
- **Original**: कलियुगमें असमर्थ लोग सूख और आनन्‍्दके नष्ट हो जानेसे प्रायः सर्वदा दुर्भिक्ष तथा क्लेश ही भोगेंगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12054)
- **Original**: कल्के आनेपर स्जेग बिना खान किये ही भोजन करेंगे, अग्नि, देवता और अतिथिका पूजन न करेंगे और न पिण्डोदक क्रिया ही करेंगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12055)
- **Original**: उस समयकी स्त्रियाँ विषयलोलुप, छोटे शरीरवाली, अति भोजन करनेवाली, अधिक सन्तान पैदा करनेवाली और मन्दभाग्या होंगी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12056)
- **Original**: ये दोनों हाथोंसे सिर खुजलाती हुई अपने गुरूुजनों और पतियोकि आदेशका अनादरपूर्वक ख़ण्डन करेंगी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12057)
- **Original**: कल्युगकी स्त्रियाँ अपना ही पेट पालनेमें तत्पर, क्षुद्र चित्तवताली, शारीरिक जौचसे हीन तथा कु और मिथ्या भाषण करनेवाली होंगी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12058)
- **Original**: उस समयकी कुलाजनाएँ निरन्तर दुश्रित्र पुरुषोंकी इच्छा रखनेवाली एवं दुराचारिणी होंगी तथा पुरुषोंके साथ असद्ब्यवहार करेंगी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12059)
- **Original**: ब्रह्मचारिगण बैदिक ब्रत आदिसे हीन रहकर हो वेदाध्ययन करेंगे तथा गृहस्थगण न तो हवन करेंगे और न सत्पात्रकों उचित दान ही देंगे। 32
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12060)
- **Original**: वानप्रस्थ [ वनके कन्द-मूलादिको छोड़कर ] आप्य भोजनक्को स्वीकार करेंगे और संन्यासी अपने मित्रादिके ख्रेह-बन्धनमें ही बैंधे रहेंगे
- **Translation**: 

---

